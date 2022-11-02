from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        # This allows us to simply automatically convert from database type
        orm_mode = True
