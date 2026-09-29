from langchain_ollama import (
    ChatOllama,
    OllamaEmbeddings
)

from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Modelo
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Banco vetorial
vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# Retriever
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
Você é um especialista em regras do futebol.

Responda apenas com base no contexto.

Se a resposta não estiver no contexto,
informe que não encontrou a informação.

Contexto:
{context}

Pergunta:
{question}
""")

# Chain
chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# Chat
while True:

    pergunta = input("\nPergunta: ")

    if pergunta.lower() == "sair":
        break

    docs = retriever.invoke(pergunta)

    print("\n=== CHUNKS RECUPERADOS ===\n")

    for i, doc in enumerate(docs, start=1):

        print(f"Chunk {i}")
        print(doc.metadata)

        print(doc.page_content[:300])

        print("\n" + "-" * 50 + "\n")

    resposta = chain.invoke(pergunta)

    print("\nResposta:\n")
    print(resposta)