from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLACHEMY_DATABASE_URL = 'sqlite:///./todos.db'
engine = create_engine(SQLACHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# we dont want to check thread all the time (false)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()

