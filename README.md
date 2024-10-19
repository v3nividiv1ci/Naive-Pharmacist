# Naive-Pharmacist

## Introduction
![Language](https://img.shields.io/badge/language-python-brightgreen)

- Designed and implemented for Assignment 1 Task 1 of [CSC6203, 2024 fall semester](https://llm-course.github.io/).
- Naive-Pharmacist leverages both conventional prompt engineering strategies and Retrieval Augmented Generation(RAG), aiming to enhance Large Language Models (LLMs)'s accuracy on the pharmacist licensure exam.
- By leveraging RAG based on enhanced pharmacy data, Naive-Pharmacist outstands with a maximum accuracy on several common LLMs, maximizing at the accuracy of 88.66% on GPT-4.
- The dataset used is [2021_pharmacist_licensure_exam](https://github.com/LLM-Course/LLM-course.github.io/tree/main/Assignments/Assignment1/task1).
## Quick Start
1. Download the prerequisites
```
pip install langchain, langchain_text_splitters, tqdm, openai, retrying, re, matplotlib
```
2. Adapt the params in ``./configs.py``
```
OPENAI_API_KEY = "your api key"
OPENAI_BASE_URL = "your base url"
```
3. Run ``./main.py``
```
python main.py
```
4. Parse & Plot
```
cd ./plot
python plot_different_models.py
```
5. See the automatically saved figs under ``./figs``, and see the log under ``./data``
