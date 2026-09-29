<div align="center">

# ⚽ Agente RAG para Regras do Futebol

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
](https://img.shields.io/badge/LangChain-LCEL-green?-badge
![Ollama](https://img.shields.io/badge/Ollama-Qwen2.5%201.5B-black?the-badge
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Storee=for-the-badge
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-red?style=-badge

Projeto desenvolvido para estudos de LangChain, Ollama, ChromaDB e RAG.

</div>

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
