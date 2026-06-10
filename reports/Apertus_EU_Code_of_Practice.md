Code of Practice for the Apertus LLM (GPAI)
---

This document contains the Code of Practice for the Apertus LLM published by the Swiss National AI Institute (SNAI), a partnership between the two Swiss Federal Institutes of Technology, ETH Zurich and EPFL, on Sept 2nd, 2025. The model is released under a free and open-source license that allows for the access, usage, modification, and distribution of the model, and whose parameters, including the weights, the information on the model architecture, and the information on model usage, are made publicly available. 

Despite the exceptions for GPAI models released under these conditions, SNAI provides this Code of Practice voluntarily for transparency purposes and for the users' convenience . The Swiss Federal Institutes have not signed the signature form provided by the EU AI ORice. The Apertus LLM is a general-purpose AI model without foreseeable systemic risk. Therefore, this Code of Practice comprises two (2) chapters: A) Transparency and B) Copyright Policy. Release Version of this CoP: v1 Last update: 01.09.2025

## A) TRANSPARENCY DOCUMENTATION (Art. 53(1)(b) EU AI Act)

The following information outlines the measures regarding transparency.

## 1) General Information

Legal name for the model provider: Both Swiss Federal Institutes of Technology, ETH Zurich and EPFL, are cooperation partners of the Swiss National AI Institute (SNAI)

[https://www.swiss-ai.org/](https://www.swiss-ai.org/)

## [llm-requests@swiss-ai.org](mailto:llm-requests@swiss-ai.org)

Authorised representative name and contact details (in EU): N/A Model family: Apertus Versioned model name: Apertus 1 Release date: Sept 2nd, 2025 Union market release: Sept 2nd, 2025 Model dependencies: None. The model is trained from scratch.

## 2) Model Properties

Model architecture: Decoder-only transformer architecture with xIELU activations, QK- Norms, Pre-Norm by RMSNorms, and rotary positional embeddings.

Input modalities: Text-only

Maximum input size: Native context length 64k tokens, extensible to 128k

Output modalities: Text-only

Maximum output size: N/A (DP dependent)

Total model size: 70 billion parameters, and 8 billion respectively

## 3) Methods of Distribution and Licenses

Distribution channels: Hugging Face

Model License: Apache 2.0 (January 2004), accessible at

https://www.apache.org/licenses/LICENSE-2.0

Additional assets made available, incl. description of access and additional licenses:

- Data processing code:
  - [github.com/swiss-ai/pretrain-data](https://github.com/swiss-ai/pretrain-data)
  - [github.com/swiss-ai/posttrain-data](https://github.com/swiss-ai/posttrain-data)
- Model pretraining code:
  - [github.com/swiss-ai/pretrain-code](https://github.com/swiss-ai/pretrain-code)
- Base &amp; instruct models as well as intermediate training checkpoints
  - [huggingface.co/swiss-ai/Apertus-8B](https://huggingface.co/swiss-ai/Apertus-8B)
  - [huggingface.co/swiss-ai/Apertus-70B](https://huggingface.co/swiss-ai/Apertus-70B)
  - [huggingface.co/swiss-ai/Apertus-8B-Instruct](https://huggingface.co/swiss-ai/Apertus-8B-Instruct)
  - [huggingface.co/swiss-ai/Apertus-70B-Instruct](https://huggingface.co/swiss-ai/Apertus-70B-Instruct)

Apertus - Democratizing Open and Compliant LLMs for Global Language

- Technical report: [Available as preprint on arXiv](https://arxiv.org/abs/2509.14233)

## 4) Use

[Acceptable Use Policy: See huggingface.co/swiss-ai](https://huggingface.co/swiss-ai/Apertus-70B-2509)

Intended uses: **General-purpose AI model**

Type and nature of AI systems in which the general-purpose AI model can be integrated: **Conversational AI Systems, AI Workflows, Research &amp; Development Tools**

Technical means for model integration: **Support for common inference frameworks, such as vLLM, SGlang, Hugging Face Transformers. See model card on Hugging Face for full details.**

Required hardware: **N/A**

Required software: **N/A**

Export Regulations: **N/A**

## 5) Information on Data Used for Training, Testing, and Validation

Training Data Type/Modality: **Text**

Latest date of data acquisition: **Main pretraining dataset knowledge cutoR is 03/2024, while some domain-specific parts of the dataset (math) and parts of the post-training datasets have a later date of collection.**

Training Data Provenance: **The following large pretraining datasets derived from CommonCrawl were used, with data from 2013 onward to a knowledge cutoR of March 2024 (CC-MAIN-2024-10). The datasets were not used as is but additionally filtered for opt-out retrospectively, for toxicity, high quality, and other preprocessing as detailed below.**

## English datasets:

[HuggingFaceFW/fineweb-edu (v1.0.0)](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)

[epfml/FineWeb-HQ](https://huggingface.co/datasets/epfml/FineWeb-HQ)

[HuggingFaceTB/dclm-edu](https://huggingface.co/datasets/HuggingFaceTB/dclm-edu)

## Multilingual datasets:

[epfml/FineWeb-HQ](https://huggingface.co/datasets/epfml/FineWeb-HQ)

[HuggingFaceFW/fineweb-2 (v2.0.1)](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)

## Code &amp; math datasets:

https://huggingface.co/datasets/bigcode/the-stack-dedup (v1.2)
https://huggingface.co/datasets/common-pile/stackv2\_edu\_filtered
https://huggingface.co/datasets/HuggingFaceTB/finemath
https://huggingface.co/datasets/LLM360/MegaMath

Other smaller publicly available and permissively text-only datasets were used in training, in particular in the post-training phase. Those were also processed by additional licence filtering and decontamination, and include:

## Wikipedia

https://huggingface.co/datasets/HuggingFaceTB/smoltalk2
https://huggingface.co/datasets/utter-project/EuroBlocks-SFT-Synthetic-1124
https://huggingface.co/datasets/allenai/tulu-3-sft-olmo-2-mixture-0225
[https://huggingface.co/datasets/DataProvenanceInitiative/Commercial-Flan-Collection-Chain-Of-Thought](https://huggingface.co/datasets/DataProvenanceInitiative/Commercial-Flan-Collection-Chain-Of-Thought)
In addition, the pretraining data contained small amounts of canary/poisoning data were added by https://spylab.ai/, as well as memorization detection traces from public domain project Gutenberg books.

Data curation methodologies: See Technical Report.

## B) COPYRIGHT POLICY (Art. 53(1)(c) EU AI Act)

The following information outlines the measures of taken to comply with copyright. In particular it identifies, and complies with, reservation of rights expressed by rightsholders.

## 1) Reproduction and extraction of lawfully accessible copyright-protected content

SNAI has implemented and adheres to the following measures to reduce and extract only lawfully accessible content for the training Apertus LLM:

The pre-training data used for the Apertus LLM was obtained in/from datasets licensed from Hugging Face (for details please refer to chapter A, above). SNAI respects technological denial and/or restriction of access imposed by copyright holders. No content from subscription models or paywalls was used (or circumvented for access purposes) for training of the Apertus LLM.

To the best of knowledge, the Apertus LLM was not trained on data recognised as persistently and repeatedly infringing copyright and related rights on a commercial scale by courts or public authorities in the European Union and the European Economic Area.

## 2) Identification and compliance with rights reservations

SNAI has identified and complied with rights reservations, including through state-of-the-art technologies and machine-readable reservations, e.g. robots.txt. The Apertus LLM was trained on web documents crawled by CommonCrawl while respecting standard machine-readable opt-out by websites. In addition, data from websites which have recently opted out by specifying at least one of the common AI crawlers, at the time of January 2025, was removed. Crucially, such removals were also applied retroactively in all earlier crawls since 2013, of each corresponding website present in our datasets. Pretraining and posttraining datasets were additionally filtered for licence compliance, and processed by PII removal (for details please refer to chapter A, above).

## 3) Mitigation of the risk of copyright-infringing outputs

To mitigate the risk that a downstream AI system, into which the Apertus LLM (AI model) is integrated, generates output that may infringe copyrights, SNAI

- implemented state-of-the-art mitigation techniques to avoid verbatim memorization in the model, by the Goldfish loss technique https://arxiv.org/html/2406.10209 , which avoids verbatim memorization of text sequences longer than 50 tokens. More precisely, every 50th token (on average) of the pretraining data is not provided a prediction target, i.e. has no loss function, and thus breaks any verbatim memorization beyond that sequence length. More detailed results on the success of this mitigation technique is provided in the model's technical report. SNAI considers these measures as appropriate and proportionate technical safeguards to prevent the Apertus LLM from generating outputs that reproduce training content (for details please refer to chapter A, above); provided, however, that downstream providers remain responsible for their AI system and its (prompted) output.
- prohibits its Apertus LLM being used for copyright infringing uses (for details please refer to chapter A, above).

## 4) Contact for the lodging of complaints

Affected right holders, i.e. right holders whose copyrighted material has been used for training purposes of the Apertus LLM and who believe their copyright has been infringed during this training process, may lodge a complaint to:

## [llm-copyright-requests@swiss-ai.org](mailto:llm-copyright-requests@swiss-ai.org)

Complaints must be sufficiently precise and adequately substantiated regarding the non-compliance of SNAI with its commitments pursuant to this chapter B and provide easily accessible information about it. SNAI will act within reasonable time from receiving a complaint in a diligent and non-arbitrary manner. SNAI reserves the right not to respond if (i) a complaint is manifestly unfounded or (ii) has already been addressed to an identical or similar complaint by the same rightsholder.

*******
