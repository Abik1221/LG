from langchain.vectorstores import chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

textspliter = RecursiveCharacterTextSplitter(chunk_size=500, chunck_overlap=50)
textspliter.split_text = lambda text: textspliter.split_text(text)

persist_directory = 'db'

embedding = OpenAIEmbeddings()

vectordb = chroma.from_documents(documents="texts",
                                 embedding= embedding,
                                 persist_directory= persist_directory
                                )

vectordb.persist()
vectordb = None

chromadb = chroma(persist_directory=persist_directory,
                  embedding_function=embedding)

retriver = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})

retriver.get_relevant_documnets("What is the capital of France?")


qa_chain = RetrievalQA.from_chain_type(
    llm = openai(),
    chain_type = "stuff",
    retriver = retriver,
    return_source_documents=True
)