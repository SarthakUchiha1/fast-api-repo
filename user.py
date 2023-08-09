from fastapi import APIRouter,Depends
from Schema import UserBase,UserDisplay
from sqlalchemy.orm import Session
from db import get_db
import db_user
from typing import List

router = APIRouter(prefix='/user',
                   tags=['user']
)


# create user 
@router.post("/",response_model= UserDisplay)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)



#read all user
@router.get('/',response_model=List[UserDisplay])
def get_all(db:Session = Depends(get_db)):
    return db_user.get_all_users(db)
