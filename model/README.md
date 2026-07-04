---
license: apache-2.0
base_model:
- swiss-ai/Apertus-v1.5-8B-2607
pipeline_tag: text-generation
library_name: transformers
tags:
  - multilingual
  - switzerland
  - compliant
  - swiss-ai
  - apertus
---

# Apertus 1.5

(TODO: update evaluation chart)

##  Table of Contents

1. [Model Summary](#model-summary)
2. [How to use](#how-to-use)
3. [Evaluation](#evaluation)
4. [Training](#training)
5. [Limitations](#limitations)
6. [Legal Aspects](#legal-aspects)

## Model Summary

Apertus is a 70B and 8B parameter language model designed to push the boundaries of fully-open multilingual and transparent models. 
The model supports over 1000 languages and long context, it uses only fully compliant and open training data, and achieves comparable performance to models trained behind closed doors.

The model is a decoder-only transformer, pretrained on 17T tokens with a staged curriculum of web, code and math data. The model uses a new xIELU activation function and the AdEMAMix optimizer. Post-training included supervised fine-tuning and alignment via QRPO, DPO and RLVR.

### Key features

- **Fully open model**: open weights + open data + full training details including all data and training recipes
- **Massively Multilingual**: 1'811 natively supported languages
- **Compliance:** Apertus is trained while respecting opt-out consent of data owners (even retroactively), avoiding memorization of training data using [Goldfish loss](https://arxiv.org/abs/2406.10209).

For more details, please refer to our [technical report](https://arxiv.org/abs/2509.14233).

## What's new

Apertus 1.5, our latest model release, builds on the strengths of previous versions: 

- Continued Pretraining: The training base has been expanded by adding 2 trillion tokens of high-quality data. Data upsampling has been performed in strategic domains critical to public interest, including Health, Education, and Justice.
- Native Audio & Image Input: Apertus 1.5 introduces multimodal support for processing audio and image inputs, enabling more intuitive and versatile interaction beyond text.
- Advanced Reasoning: Enhanced logical reasoning capabilities allow the model to handle more complex, multi-step queries.
- Improved Instruction-Following: Significant improvements in instruction adherence ensure more predictable and accurate responses to user prompts.

We are working with inference providers to ensure global availability on multiple platforms at launch. These will be linked in our [Get Started page](https://apertvs.ai/pages/get-started/).

See also the [Apertus 1.1 "Mini"](https://huggingface.co/collections/swiss-ai/apertus-mini) collection of smaller distilled versions of the original model.


## How to use

Users of Apertus can find tips on getting started with desktop software and cloud providers on our website. Please visit the [Get Started section](https://apertus-ai.org/pages/get-started/) page if you are interested to try the model.

Detailed instructions for advanced usage can be found in the [User Guides](https://apertvs.ai/docs/guides/).

### Developers

For data science users, the modeling code for Apertus is available from [Transformers](https://huggingface.co/docs/transformers/index) `v4.56.0` and later, and we recommend you upgrade to the latest stable version. We have tested up to `v5.12.1` in this release. A code example of using the model in this way is listed below.

Run a command like this first to install the library using a package manager:

```bash
pip install -U transformers
```

With this sample Python code, you can load and prompt Apertus in the library from Hugging Face:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "swiss-ai/Apertus-8B-Instruct-2509"
device = "cuda"  # for GPU usage or "cpu" for CPU usage

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
).to(device)

# prepare the model input
prompt = "Give me a brief explanation of gravity in simple terms."
messages_think = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages_think,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt", add_special_tokens=False).to(model.device)

# Generate the output
generated_ids = model.generate(**model_inputs, max_new_tokens=32768)

# Get and decode the output
output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

>[!TIP]
> We recommend setting `temperature=0.8` and `top_p=0.9` in the sampling parameters.

### Long context processing

Apertus 1.5 by default supports a context length up to 262'144 tokens, a four-fold increase from our initial release.

(#TODO mention something about performance tradeoffs)

### Agentic Usage

Apertus supports tool use with newer versions of the internal parser, such as the version shipped with [vLLM 0.22.0](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) and above. 

(#TODO recommendations on tool use and harnesses)

## Deployment

Deployment of the models is directly supported in a variety of open source frameworks, such as [Transformers](https://github.com/huggingface/transformers), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), and also for running on-device with [MLX](https://github.com/ml-explore/mlx-lm) or [GGUF](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) as loading formats. 

For instance, the Apertus tool parser is available in current releases of vLLM, and we have tested `v0.24.0` at the time of release. 
A Docker image for vllm [is available](https://github.com/swiss-ai/model-launch/pkgs/container/vllm_apertus_1.5), as well as deployment instructions for this and other software on [our documentation site](https://apertus-ai.org/docs/guides/).

There is a diverse community creating quantized and reformatted versions of the Apertus models. We will endeavor to support the main formats with an official build on the [@swiss-ai](https://huggingface.co/swiss-ai) Hugging Face organization. Verified community versions are linked from our documentation. 

Please use 3rd party builds at your own risk, and contact us for a quick validation before going to production. 

## Evaluation

Benchmark evaluations, for pretraining and posttraining phases, multilingual evaluations in around hundred languages, and long context evaluations are provided in Section 5 of the [Apertus Tech Report](https://arxiv.org/abs/2509.14233)

(#TODO update with link to benchmarks page)

## Training

### Model

- **Architecture:** Transformer decoder
- **Pretraining tokens:** 17T
- **Precision:** bfloat16

### Software & hardware

- **GPUs:** 4096 GH200
- **Training Framework:** [Megatron-LM](https://github.com/swiss-ai/Megatron-LM)
- ... (#TODO what else?)

### Open resources

All elements used in the training process are made openly available
- **Training data reconstruction scripts:** [github.com/swiss-ai/pretrain-data](https://github.com/swiss-ai/pretrain-data)
- The training intermediate checkpoints are available on the different branches of this same repository

(#TODO posttraining data etc.)

## Limitations

Apertus can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.

(#TODO link to Swiss AI Charter?)

## Legal Aspects

#### EU AI Act Transparency Documentation and Code of Practice

These are being updated for Apertus 1.5. For documentation of the initial release, see:

- [Apertus_EU_Public_Summary.pdf](https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/Apertus_EU_Public_Summary.pdf)
- [Apertus_EU_Code_of_Practice.pdf](https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/Apertus_EU_Code_of_Practice.pdf)

(#TODO update these links)

#### Data Protection and Copyright Requests

For removal requests of personally identifiable information (PII) or of copyrighted content, please contact the respective dataset owners or us directly:

- llm-privacy-requests@swiss-ai.org
- llm-copyright-requests@swiss-ai.org
  
Currently no output filter is provided. We endeavour to address data protection deletion requests by updating filters in our data pipeline, and providing regular (at least bi-annual) releases to the model weights. We strongly advise downloading and updating new model weights from this site every six months.

## Contact

To contact us, please use the links at https://apertus-ai.org/contact/ - or send an email to
llm-requests@swiss-ai.org

## Citation

```bash
@misc{swissai2025apertus,
  title={{Apertus: Democratizing Open and Compliant LLMs for Global Language Environments}},
  author={Alejandro Hernández-Cano and Alexander Hägele and Allen Hao Huang and Angelika Romanou and Antoni-Joan Solergibert and Barna Pasztor and Bettina Messmer and Dhia Garbaya and Eduard Frank Ďurech and Ido Hakimi and Juan García Giraldo and Mete Ismayilzada and Negar Foroutan and Skander Moalla and Tiancheng Chen and Vinko Sabolčec and Yixuan Xu and Michael Aerni and Badr AlKhamissi and Ines Altemir Marinas and Mohammad Hossein Amani and Matin Ansaripour and Ilia Badanin and Harold Benoit and Emanuela Boros and Nicholas Browning and Fabian Bösch and Maximilian Böther and Niklas Canova and Camille Challier and Clement Charmillot and Jonathan Coles and Jan Deriu and Arnout Devos and Lukas Drescher and Daniil Dzenhaliou and Maud Ehrmann and Dongyang Fan and Simin Fan and Silin Gao and Miguel Gila and María Grandury and Diba Hashemi and Alexander Hoyle and Jiaming Jiang and Mark Klein and Andrei Kucharavy and Anastasiia Kucherenko and Frederike Lübeck and Roman Machacek and Theofilos Manitaras and Andreas Marfurt and Kyle Matoba and Simon Matrenok and Henrique Mendoncça and Fawzi Roberto Mohamed and Syrielle Montariol and Luca Mouchel and Sven Najem-Meyer and Jingwei Ni and Gennaro Oliva and Matteo Pagliardini and Elia Palme and Andrei Panferov and Léo Paoletti and Marco Passerini and Ivan Pavlov and Auguste Poiroux and Kaustubh Ponkshe and Nathan Ranchin and Javi Rando and Mathieu Sauser and Jakhongir Saydaliev and Muhammad Ali Sayfiddinov and Marian Schneider and Stefano Schuppli and Marco Scialanga and Andrei Semenov and Kumar Shridhar and Raghav Singhal and Anna Sotnikova and Alexander Sternfeld and Ayush Kumar Tarun and Paul Teiletche and Jannis Vamvas and Xiaozhe Yao and Hao Zhao Alexander Ilic and Ana Klimovic and Andreas Krause and Caglar Gulcehre and David Rosenthal and Elliott Ash and Florian Tramèr and Joost VandeVondele and Livio Veraldi and Martin Rajman and Thomas Schulthess and Torsten Hoefler and Antoine Bosselut and Martin Jaggi and Imanol Schlag},
  year={2025},
  howpublished={\url{https://arxiv.org/abs/2509.14233}}
}
```
