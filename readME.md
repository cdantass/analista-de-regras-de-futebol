# ⚽ Agente RAG para Regras do Futebol

<p align="center">

![Python](https://img.shields.io/badge13-blue?style=for-the-badge&logo=python

![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)

s://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge)

(https://img.shields.io/badge/ChromaDB-Vector%20Database-orange?style=for-thecense](https://img.shields.io/badge/License-MIT-purple?style=for-the>

---

## 📖 Sobre o Projeto

Este projeto implementa um sistema **RAG (Retrieval-Augmented Generation)** utilizando **LangChain**, **ChromaDB** e **Ollama** para responder perguntas sobre as regras do futebol com base em um PDF oficial.

Ao invés de depender apenas do conhecimento do modelo, o sistema consulta documentos previamente indexados para gerar respostas mais confiáveis.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python
- 🦜 LangChain
- 🧠 Ollama
- 📚 ChromaDB
- ⚡ Qwen2.5 1.5B
- 🔍 Nomic Embed Text
- 📄 PyPDF

---

## 🏗️ Arquitetura

```text
PDF
 ↓
PyPDFLoader
 ↓
Documents
 ↓
Chunks
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retriever
 ↓
Prompt
 ↓
Qwen2.5:1.5b
 ↓
Resposta
``