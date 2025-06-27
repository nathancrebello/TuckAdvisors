# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connection string
DATABASE_URL = "sqlite:///./gptOutput.db"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# session factory    
LocalSession = sessionmaker(autocommit = False, autoflush=False, bind=engine)
# base class
Base = declarative_base() 