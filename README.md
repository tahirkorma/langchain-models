# LangChain Models

A comprehensive repository showcasing the integration of various **Language Models (LLMs)**, **Chat Models**, and **Embedding Models** using the latest version of [LangChain](https://github.com/langchain-ai/langchain).

## 🔍 Overview

This project demonstrates how to leverage both **open-source** and **closed-source** models from providers such as **OpenAI**, **Anthropic**, **Google**, and **Hugging Face**, as well as locally hosted models running on your own system. Built using the **latest LangChain release**, it provides a modular framework for experimenting with and combining different model types.

---

## 🧠 Language Models (LLMs)

> ⚠️ Traditional LLMs are gradually being replaced in many applications by **chat-optimized models**, which provide better instruction-following and contextual interactions.

LLMs refer to general-purpose large language models that take a prompt as input and return a text completion. Examples include:

- **OpenAI GPT-3 (text-davinci-003)**  
- **Google PaLM API**
- **Anthropic Claude (non-chat versions)**
- **Open-source models on Hugging Face** (e.g., `EleutherAI/gpt-j`, `bigscience/bloom`)

These models can still be useful for straightforward completions and basic NLP tasks, but **Chat Models** are now the preferred choice for most interactive or task-specific use cases.

---

## 💬 Chat Models

Chat Models are fine-tuned versions of LLMs optimized for dialogue-based interactions. They support **multi-turn conversations**, **tool usage**, and **function calling** in LangChain workflows.

Examples include:

- **OpenAI GPT-4 / GPT-3.5 Turbo**
- **Anthropic Claude 3**
- **Google Gemini Pro**
- **Local chat-tuned models** like `mistralai/Mistral-7B-Instruct`, `Meta-Llama-3`, or `Nous Hermes` variants

These models are ideal for agents, conversational interfaces, and structured workflows in LangChain.

---

## 📌 Embedding Models

Embedding models convert text into vector representations, enabling powerful capabilities like semantic search, retrieval-augmented generation (RAG), clustering, and more.

Examples used in this repo:

- **OpenAI Embeddings (e.g., `text-embedding-3-large`)**
- **Local embedding models** like `sentence-transformers/all-MiniLM-L6-v2`

LangChain makes it easy to switch between embedding providers and manage vector stores across different backends.

---

## ⚙️ Supported Model Sources

- ✅ **Open Source**: Hugging Face models, local GGUF/transformer models
- ✅ **Closed Source**: OpenAI, Anthropic, Google APIs
- ✅ **Local Execution**: Models running via `llama.cpp`, `ctransformers`, or `transformers` on your own hardware

---

## 🧱 Built with

- [LangChain (latest version)](https://github.com/langchain-ai/langchain)
- [Python 3.10+](https://www.python.org/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Google Generative AI SDK](https://github.com/google/generative-ai-python)
