from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


SQLAlchemyDATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(SQLAlchemyDATABASE_URL, connect_args={"check_same_thread": False})



sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()