from transformers import LlamaTokenizer, AutoModelForCausalLM, AutoConfig, GenerationConfig
import torch

ckpt_path = '/workspace/BELLE-train/Version_raw/'
load_type = torch.float16
device = torch.device(0)
tokenizer = LlamaTokenizer.from_pretrained(ckpt_path)
tokenizer.pad_token_id = 0
tokenizer.bos_token_id = 1
tokenizer.eos_token_id = 2
tokenizer.padding_side = "left"
model_config = AutoConfig.from_pretrained(ckpt_path)
model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=load_type, config=model_config)
model.to(device)
model.eval()

prompt = "Human: 请把下列标题扩写成摘要, 不少于100字: 基于视觉语言多模态的实体关系联合抽取的研究 \n\nAssistant: "
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"].to(device)
generation_config = GenerationConfig(
    temperature=0.1,
    top_p=0.75,
    top_k=40,
    num_beams=1,
    bos_token_id=1,
    eos_token_id=2,
    pad_token_id=0,
    max_new_tokens=128,
    min_new_tokens=10,
    do_sample=True,
)
with torch.no_grad():
    generation_output = model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        repetition_penalty=1.2,
    )
    output = generation_output.sequences[0]
    output = tokenizer.decode(output, skip_special_tokens=True)
    print(output)
