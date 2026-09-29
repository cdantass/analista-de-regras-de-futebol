from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

PDF_PATH = "pdf/regras.pdf"

# Carrega PDF
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

print(f"Páginas carregadas: {len(documents)}")

# Cria chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Chunks criados: {len(chunks)}")

# Embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Banco vetorial
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Banco vetorial criado com sucesso!")