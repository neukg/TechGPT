import sys
import hashlib
import os
import argparse as argparse


def xor_bytes(data, key):
    return bytes(a ^ b for a, b in zip(data, (key * (len(data) // len(key) + 1))[:len(data)]))


def xor_worker(task_queue, result_queue):
    while True:
        chunk_idx, data, key = task_queue.get()
        result_queue.put((chunk_idx, xor_bytes(data, key)))
        task_queue.task_done()


def write_result_chunk(fp, w_chunk_idx, pending, hasher):
    if not pending:
        return w_chunk_idx, pending
    pending.sort()
    for pending_idx, (chunk_idx, chunk) in enumerate(pending):
        if chunk_idx != w_chunk_idx:
            return w_chunk_idx, pending[pending_idx:]
        fp.write(chunk)
        hasher.update(chunk)
        w_chunk_idx += 1
    return w_chunk_idx, []


def decrypt(input_file, key_file, output_dir):
    print(f"Decrypting file {input_file}")

    chunk_size = 10 * 1024 * 1024
    key_chunk_size = 10 * 1024 * 1024

    hasher = hashlib.sha256()

    # Get the checksum from the input file name
    input_file_basename = os.path.basename(input_file)
    checksum_hex = input_file_basename.split('.')[-2]

    with open(input_file, "rb") as in_file, open(key_file, "rb") as key_file:
        # Get the size of the input file
        file_size = os.path.getsize(input_file)

        # Read the input file
        input_data = in_file.read()

        # Create the output file path without the checksum in the filename
        output_file = os.path.join(output_dir, input_file_basename.split('.' + checksum_hex)[0])

        with open(output_file, "wb") as out_file:
            r_chunk_idx = 0  # how many chunks we have read
            w_chunk_idx = 0  # how many chunks have been written
            write_pending = []  # have xor results, awaiting to be written to file

            bytes_read = 0
            while True:
                chunk = input_data[:chunk_size]
                input_data = input_data[chunk_size:]

                if not chunk:
                    break

                key_chunk = key_file.read(key_chunk_size)
                if not key_chunk:
                    key_file.seek(0)
                    key_chunk = key_file.read(key_chunk_size)
                write_pending.append((r_chunk_idx, xor_bytes(chunk, key_chunk)))

                w_chunk_idx_new, write_pending = write_result_chunk(out_file, w_chunk_idx, write_pending, hasher)

                bytes_read += (w_chunk_idx_new - w_chunk_idx) * chunk_size
                progress = bytes_read / file_size * 100
                sys.stdout.write(f"\rProgress: {progress:.2f}%")
                sys.stdout.flush()

                w_chunk_idx = w_chunk_idx_new
                r_chunk_idx += 1

            # wait for xor workers
            sys.stdout.write('\rWaiting for workers...')
            sys.stdout.flush()

            sys.stdout.write('\rWriting final chunks...')
            sys.stdout.flush()
            write_result_chunk(out_file, w_chunk_idx, write_pending, hasher)
            computed_hash = hasher.digest()

            print(f"Checksum: {computed_hash.hex()}")

        print("Decryption completed.")


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--type', choices=['encrypt', 'decrypt'], required=True)
    argparse.add_argument("--input_file", type=str, required=True)
    argparse.add_argument("--key_file", type=str, required=True)
    argparse.add_argument("--output_dir", type=str, required=True)
    args = argparse.parse_args()
    if args.type == 'decrypt':
        decrypt(args.input_file, args.key_file, args.output_dir)
    elif args.type == 'encrypt':
        pass
    else:
        print('Unknown type')
