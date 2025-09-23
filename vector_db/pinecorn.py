from langchain.vectorstores import chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


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