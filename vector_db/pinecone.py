from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.vectorstores import pinecone
from langchain.chains import retrieval_qa
from langchain.prompts import PromptTemplate
import os

loader = PyPDFDirectoryLoader("pdfs")
data = loader.Load()

text_spliter = RecursiveCharacterTextSplitter(chunk = 500, chunck_overlap = 50)

text_cuhunks = text_spliter.split_documents(data)

os.environ['OPENAI_API_KEY'] = 'your_openai_api_key_here'
os.environ['PINECONE_API_KEY'] = 'your_pinecone_api_key_here'
os.environ['PINECONE_ENVIRONMENT'] = 'your_pinecone_environment_here'
embeddings = OpenAIEmbeddings()

embeddings.embed_query = "hello"

docsearch = pinecone.from_texts(
    [text.page_content for text in text_cuhunks],
    embeddings,
    index_name="your_pinecone_index_name_here"
)

