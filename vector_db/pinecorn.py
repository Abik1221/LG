from langchain.vectorstores import chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


