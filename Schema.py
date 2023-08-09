from pydantic import BaseModel
class UserBase(BaseModel): #datatype provided to us by user 
    username : str
    email :str
    password : str



class UserDisplay(BaseModel):
    username:str
    email:str

    class Config():
        orm_mode = True