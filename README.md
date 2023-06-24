


# TechGPT: Technology-Oriented Generative Pretrained Transformer
Demo: [TechGPT-neukg](http://techgpt.neukg.com) <br>
HuggingFace🤗: [neukg/TechGPT-7B](https://huggingface.co/neukg)

<div align="center">

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/neukg/TechGPT/blob/main/LICENSE)
[![Generic badge](https://img.shields.io/badge/🤗-Huggingface%20Repo-green.svg)](https://huggingface.co/neukg)
</div>


## 简介 Introduction
TechGPT是[“东北大学知识图谱研究组”](http://faculty.neu.edu.cn/renfeiliang)发布的垂直领域大语言模型。<br>
主要强化了如下三类任务:
- 以“知识图谱构建”为核心的关系三元组抽取等各类信息抽取任务
- 以“阅读理解”为核心的各类智能问答任务。
- 以“文本理解”为核心的关键词生成等各类序列生成任务。

在这三大自然语言处理核心能力之内，TechGPT还具备了对计算机科学、材料、机械、冶金、金融和航空航天等十余种垂直专业领域自然语言文本的处理能力。
目前，TechGPT通过提示和指令输入方式的不同，支持单轮对话和多轮对话，涵盖了领域术语抽取、命名实体识别、关系三元组抽取、文本关键词生成、标题生成摘要、摘要生成标题、文本领域识别、机器阅读理解、基础常识问答、基于上下文的知识问答、建议咨询类问答、文案生成、中英互译和简单代码生成等多项自然语言理解和生成能力。

---
TechGPT mainly strengthens the following three types of tasks:
- Various information extraction tasks such as relation triplet extraction with "knowledge graph construction" as the core
- Various intelligent question-and-answer tasks centered on "reading comprehension".
- Various sequence generation tasks such as keyword generation with "text understanding" as the core.
Within these three core natural language processing capabilities, TechGPT also has the ability to process natural language texts in more than ten vertical professional fields such as computer science, materials, machinery, metallurgy, finance, and aerospace.
TechGPT supports single-round dialogue and multi-round dialogue through different input methods of prompts and instructions, covering domain term extraction, named entity recognition, relation triplet extraction, text keyword generation, title generation abstract, abstract generation title, text field Recognition, machine reading comprehension, basic common sense question and answer, context-based knowledge question and answer, suggestion consultation question and answer, copy generation, CM-EN translation and simple code generation and many other natural language understanding and generation capabilities.

## 模型功能 Model Capabilities

模型在保留基本的对话和翻译能力之外，重点强化了基于**TechKG**的数据内容，因此，**TechGPT**更擅长在计算机科学等专业领域，完成实体及实体类型抽取、关系三元组抽取、标题扩写、摘要缩写、关键词生成和机器阅读理解等任务。
下面展示了TechGPT的几个核心能力。

1. **命名实体识别**
<table>   <colgroup>     <col style="width:60%">     <col style="width:40%">   </colgroup>   <tr>     <td>问题</td>     <td>回复</td> </tr>
  <tr>     <td>抽取出下面文本的实体和实体类型：<br/>《女人树》，国产电视剧，由导演田迪执导，根据作家子页的原著改编，故事从1947年开始，跨越了解放战争和建国初期两大历史时期，展现了战斗在隐形战线上的人民英雄是如何不惧怕任何危险，不计较个人牺牲，甚至不顾人民内部的误解和生死裁决，都不暴露个人真实身份，至死不渝，与敌人周旋到底的英雄故事。</td>     <td>实体名: 女人树， 实体类型：影视作品<br/>实体名: 田迪， 实体类型：人物<br/>实体名: 子页， 实体类型：人物<br/>实体名: 1947年， 实体类型：Date</td> </tr>
</table>

2. **关系三元组抽取**
<table>   <colgroup>     <col style="width:60%">     <col style="width:40%">   </colgroup>   <tr>     <td>问题</td>     <td>回复</td> </tr>
  <tr>     <td>
请抽取出下面的关系三元组：<br>陈奕迅（Eason Chan），1974年7月27日出生于香港，中国香港流行乐男歌手、演员，毕业于英国金斯顿大学。     1995年因获得第14届新秀歌唱大赛冠军而正式出道。2005年发行的歌曲《浮夸》成为其歌唱生涯的代表作品之一。</td>     <td><陈奕迅, 出生日期, 1974年><br><陈奕迅, 出生地, 香港><br>
<陈奕迅, 毕业院校, 英国金斯顿大学><br>
<陈奕迅, 国籍, 中国></td> </tr>
</table>

3. **标题扩写**
<table>   <colgroup>     <col style="width:60%">     <col style="width:40%">   </colgroup>   <tr>     <td>问题</td>     <td>回复</td> </tr>
  <tr>     <td>请把下列标题扩写成摘要, 不少于100字: 基于视觉语言多模态的实体关系联合抽取的研究。</td>     <td>本文介绍了一种基于视觉语言的多模态实体关系联合抽取出方法。该方法利用了图像和文本之间的语义联系，通过将图像中的物体与相应的文本描述进行匹配来识别实体之间的关系。同时，本文还提出了一种新的模型结构——深度双向编码器-解码器网络（BiDAN），用于实现这种联合提取任务。实验结果表明，所提出的方法在多个数据集上取得了较好的性能表现，证明了其有效性和实用性。</td> </tr>
</table>

4. **摘要缩写**
<table>   <colgroup>     <col style="width:60%">     <col style="width:40%">   </colgroup>   <tr>     <td>问题</td>     <td>回复</td> </tr>
  <tr>     <td>请把下列摘要缩写成标题:本文介绍了一种基于视觉语言的多模态实体关系联合抽取出方法。该方法利用了图像和文本之间的语义联系，通过将图像中的物体与相应的文本描述进行匹配来识别实体之间的关系。同时，本文还提出了一种新的模型结构——深度双向编码器-解码器网络（BiDAF），用于实现这种联合提取任务。实验结果表明，所提出的方法在多个数据集上取得了较好的性能表现，证明了其有效性和实用性。</td>     <td>基于视觉语言的多模态实体关系联合抽取研究。</td> </tr>
</table>

5. **关键词生成**
<table>   <colgroup>     <col style="width:60%">     <col style="width:40%">   </colgroup>   <tr>     <td>问题</td>     <td>回复</td> </tr>
  <tr>     <td>请提取下面文本中的关键词。<br>本体是一种重要的知识库,其包含的丰富的语义信息可以为问答系统、信息检索、语义Web、信息抽取等领域的研究及相关应用提供重要的支持.因而,如何快速有效地构建本体具有非常重要的研究价值.研究者们分别从不同角度提出了大量有效地进行本体构建的方法.一般来讲,这些本体构建方法可以分为手工构建的方法和采用自动、半自动技术构建的方法.手工本体的方法往往需要本体专家参与到构建的整个过程,存在着构建成本高、效率低下、主观性强、移植不便等缺点,因而,此类方法正逐步被大量基于自动、半自动技术的本体构建方法所代替.自动、半自动构建的方法不需要（或仅需少量）人工参与,可以很方便地使用其它研究领域（如机器学习、自然语言处理等）的最新研究成果,也可以方便地使用不同数据源进行本体构建.</td>     <td>本体，知识库，问答系统，信息检索，语义 Web，信息抽取，统计主导，语言分析主导，术语抽取，概念抽取，关系抽取，本体形成，评价方法，本体构建系统</td> </tr>
</table>

6. **机器阅读理解**
<table>   <colgroup>     <col style="width:60%">     <col style="width:40%">   </colgroup>   <tr>     <td>问题</td>     <td>回复</td> </tr>
  <tr>     <td>请问这起交通事故是谁的责任居多?<br>小车和摩托车发生事故，在无红绿灯的十字路口，小停车看看左右，在觉得安全的情况下刹车慢慢以时速10公里左右的速度靠右行驶过路口，好没有出到十字路口正中时，被左边突然快速行驶过来的摩托车撞在车头前，  摩托车主摔到膝盖和檫伤脸部，请问这起交通事故是谁的责任居多。</td> <td>根据提供的信息，我们可以得出以下结论：<br>
1. 小车司机应该先观察交通信号灯是否亮起，如果没有信号灯，则应减速慢行通过交叉路口；<br>2. 在没有信号灯的交叉口中，小车的驾驶员应该在确保安全的前提下选择右侧车道行驶，以避免与来自左侧的车辆相撞；
3. 由于事故发生地点是十字路口，因此可以确定该事故属于道路交通事故范畴。<br>根据以上分析，我认为这起交通事故的主要责任在于摩托车驾驶人的行为。因为摩托车驾驶员在没有信号灯的情况下从左侧冲过来，导致与小车在十字路口相遇，造成了伤害。
然而，我们也需要考虑其他因素的影响，例如小车的速度、路面状况等。如果小车的车速过快或者路面湿滑，也可能对事故的发生产生影响。但是，由于提供的信息中没有提到这些细节，所以我们只能基于上述基本判断来回答这个问题。</td>
  </tr>
</table>

## 准备工作 Preparation

由于LLaMA开源协议的限制，本模型仅限于研究和学习用途使用。请严格遵守LLaMA的使用要求和规范。为了确保这一点，我们需要确认您具有LLaMA的原始权重，并来自完全合法渠道。

---
According to the limitations of the LLaMA open source agreement, this model is limited to research and learning purposes. Please strictly abide by the usage requirements and specifications of LLaMA. To ensure this, we need to confirm that you have LLaMA's original weight and come from a completely legitimate source.

1. 你需要先下载模型到本地，并校验它们的检查和：
```
md5sum ./*
6b2b545ff7bacaeec6297198b4b745dd  ./config.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
4ba9cc7f11df0422798971bc962fe076  ./generation_config.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
560b35ffd8a7a1f5b2d34a94a523659a  ./pytorch_model.bin.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
85ae4132b11747b1609b8953c7086367  ./special_tokens_map.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
953dceae026a7aa88e062787c61ed9b0  ./tokenizer_config.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
e765a7740a908b5e166e95b6ee09b94b  ./tokenizer.model.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
```

2. 根据这里→的[指定脚本](https://github.com/neukg/TechGPT/blob/main/utils/decrypt.py)解码模型权重：
```shell
for file in $(ls /path/encrypt_weight); do
  python decrypt.py --type decrypt \
    --input_file /path/encrypt_weight/"$file" \
    --output_dir /path/to_finetuned_model \
    --key_file /path/to_original_llama_7B/consolidated.00.pth
done
```

请将 `/path/encrypt_weight`替换为你下载的加密文件目录，把`/path/to_original_llama_7B`替换为你已有的合法LLaMA-7B权重目录，里面应该有原LLaMA权重文件`consolidated.00.pth`，将 `/path/to_finetuned_model` 替换为你要存放解码后文件的目录。
在解码完成后，应该可以得到以下文件：
```shell
./config.json
./generation_config.json
./pytorch_model.bin
./special_tokens_map.json
./tokenizer_config.json
./tokenizer.model
```

3. 请检查所有文件的检查和是否和下面给出的相同, 以保证解码出正确的文件：
```
md5sum ./*
6d5f0d60a6e36ebc1518624a46f5a717  ./config.json
2917a1cafb895cf57e746cfd7696bfe5  ./generation_config.json
0d322cb6bde34f7086791ce12fbf2bdc  ./pytorch_model.bin
15f7a943faa91a794f38dd81a212cb01  ./special_tokens_map.json
08f6f621dba90b2a23c6f9f7af974621  ./tokenizer_config.json
6ffe559392973a92ea28032add2a8494  ./tokenizer.model
```
---
1. Git clone this model first.
```
md5sum ./*
6b2b545ff7bacaeec6297198b4b745dd  ./config.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
4ba9cc7f11df0422798971bc962fe076  ./generation_config.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
560b35ffd8a7a1f5b2d34a94a523659a  ./pytorch_model.bin.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
85ae4132b11747b1609b8953c7086367  ./special_tokens_map.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
953dceae026a7aa88e062787c61ed9b0  ./tokenizer_config.json.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
e765a7740a908b5e166e95b6ee09b94b  ./tokenizer.model.e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.enc
```
2. Decrypt the files using the scripts in https://github.com/neukg/TechGPT/blob/main/utils/decrypt.py
You can use the following command in Bash.
Please replace `/path/to_encrypted` with the path where you stored your encrypted file, 
replace `/path/to_original_llama_7B` with the path where you stored your original LLaMA-7B file `consolidated.00.pth`, 
and replace `/path/to_finetuned_model` with the path where you want to save your final trained model.
```bash
for file in $(ls /path/encrypt_weight); do
  python decrypt.py --type decrypt \
    --input_file /path/encrypt_weight/"$file" \
    --output_dir /path/to_finetuned_model \
    --key_file /path/to_original_llama_7B/consolidated.00.pth
done
```
After executing the aforementioned command, you will obtain the following files.
```
./config.json
./generation_config.json
./pytorch_model.bin
./special_tokens_map.json
./tokenizer_config.json
./tokenizer.model
```
3. Check md5sum
You can verify the integrity of these files by performing an MD5 checksum to ensure their complete recovery.
Here are the MD5 checksums for the relevant files:
```
md5sum ./*
6d5f0d60a6e36ebc1518624a46f5a717  ./config.json
2917a1cafb895cf57e746cfd7696bfe5  ./generation_config.json
0d322cb6bde34f7086791ce12fbf2bdc  ./pytorch_model.bin
15f7a943faa91a794f38dd81a212cb01  ./special_tokens_map.json
08f6f621dba90b2a23c6f9f7af974621  ./tokenizer_config.json
6ffe559392973a92ea28032add2a8494  ./tokenizer.model
```

## 使用方法 Model Usage

请注意在**训练**和**推理**阶段, 模型接收的输入格式是一致的：

Please note that the input should be formatted as follows in both **training** and **inference**.

``` python
Human: {input} \n\nAssistant:
```

请在使用TechGPT之前保证你已经安装好`transfomrers`和`torch`：

```shell
pip install transformers
pip install torch
```

- 注意，必须保证安装的 `transformers` 的版本中已经有 `LlamaForCausalLM` 。<br>
- Note that you must ensure that the installed version of `transformers` already has `LlamaForCausalLM`.

[Example:](https://github.com/neukg/TechGPT/blob/main/inference.py)

``` python
from transformers import LlamaTokenizer, AutoModelForCausalLM, AutoConfig, GenerationConfig
import torch

ckpt_path = '/path/to_finetuned_model/'
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

```

输出：

```
Human: 请把下列标题扩写成摘要, 不少于100字: 基于视觉语言多模态的实体关系联合抽取的研究 

Assistant: 文本：基于视觉语言的多模态的实体关系联合抽取是自然语言处理领域中的一个重要问题。该文提出了一种新的方法，
利用深度学习技术来提取图像中的语义信息，并使用这些信息来识别和抽取图像中的人、物、地点等实体之间的关系。实验结果表明，
该方法在多个基准数据集上取得了很好的性能表现，证明了其有效性和实用性。
```

## 主要贡献者 Contributors
排名不分先后
<table>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/37218117?v=4" alt="Contributor 1" height="150">
      <br>
      <b>Adaning @ Northeastern University</b>
      <br>
      TechGPT项目的核心开发成员
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/38159292?v=4" alt="Contributor 2" height="150">
      <br>
      <b>Asimok @ Northeastern University</b>
      <br>
      TechGPT项目的核心开发成员
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/105141916?v=4" alt="Contributor 3" height="150">
      <br>
      <b>abel-nlp @ Northeastern University</b>
      <br>
      TechGPT项目的核心开发成员
    </td>
  </tr>
  </table>


## 免责声明 Disclaimers

该项目仅供学习交流使用，禁止用于商业用途。在使用过程中，使用者需认真阅读并遵守以下声明:

1. 本项目仅为大模型测试功能而生，使用者需自行承担风险和责任，如因使用不当而导致的任何损失或伤害，本项目概不负责。
2. 本项目中出现的第三方链接或库仅为提供便利而存在，其内容和观点与本项目无关。使用者在使用时需自行辨别，本项目不承担任何连带责任；
3. 使用者在测试和使用模型时，应遵守相关法律法规，如因使用不当而造成损失的，本项目不承担责任，使用者应自行承担；若项目出现任何错误，请向我方反馈，以助于我们及时修复；
4. 本模型中出现的任何违反法律法规或公序良俗的回答，均不代表本项目观点和立场，我们将不断完善模型回答以使其更符合社会伦理和道德规范。

使用本项目即表示您已经仔细阅读、理解并同意遵守以上免责声明。本项目保留在不预先通知任何人的情况下修改本声明的权利。

---

This project is for learning exchange only, commercial use is prohibited. During use, users should carefully read and abide by the following statements:

1. This project is only for the test function of the large model, and the user shall bear the risks and responsibilities. This project shall not be responsible for any loss or injury caused by improper use.
2. The third-party links or libraries appearing in this project exist only for convenience, and their content and opinions have nothing to do with this project. Users need to identify themselves when using it, and this project does not bear any joint and several liabilities;
3. Users should abide by the relevant laws and regulations when testing and using the model. If the loss is caused by improper use, the project will not bear the responsibility, and the user should bear it by themselves; if there is any error in the project, please feedback to us. to help us fix it in a timely manner;
4. Any answers in this model that violate laws and regulations or public order and good customs do not represent the views and positions of this project. We will continue to improve the model answers to make them more in line with social ethics and moral norms.

Using this project means that you have carefully read, understood and agreed to abide by the above disclaimer. The project reserves the right to modify this statement without prior notice to anyone.

## 引用 Citation

如果使用本项目的代码、数据或模型，请引用本项目。

Please cite our project when using our code, data or model.

```
@misc{TechGPT,
  author = {Feiliang Ren, Ning An, Qi Ma, Hei Lei},
  title = {TechGPT: Technology-Oriented Generative Pretrained Transformer},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/neukg/TechGPT}},
}
```

**我们对BELLE的工作表示衷心的感谢！**

**Our sincere thanks to BELLE for their work!**

```
@misc{ji2023better,
      title={Towards Better Instruction Following Language Models for Chinese: Investigating the Impact of Training Data and Evaluation}, 
      author={Yunjie Ji and Yan Gong and Yong Deng and Yiping Peng and Qiang Niu and Baochang Ma and Xiangang Li},
      year={2023},
      eprint={2304.07854},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc{BELLE,
  author = {Yunjie Ji, Yong Deng, Yan Gong, Yiping Peng, Qiang Niu, Baochang Ma, Xiangang Li},
  title = {BELLE: Be Everyone's Large Language model Engine},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/LianjiaTech/BELLE}},
}
```
