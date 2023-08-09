from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# SQLALCHEMY_DB_URL =  "sqlite:///./fastapi-practice.db"

# MY SQL 
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234mom@localhost/db3"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base() # base is used for creating models 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()