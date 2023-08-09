from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from sqlalchemy import Column
from db import Base,engine,SessionLocal

class DBUser(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))