from pydantic import BaseModel
from typing import List

# schemas/item.py
# schemas/user.py
class AnswerBase(BaseModel):
    question_id: int
    chosen_answer: str

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    chosen_answer: str | None = None
    
class Answer(AnswerBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ParticipantBase(BaseModel):
    email: str
    name:str
    age:int
    gender:str
class Participant(ParticipantBase):
    id: int    
    answers: List[Answer]

    class Config:
        orm_mode = True

class ParticipantCreate(ParticipantBase):
    password: str
    

class ParticipantUpdate(ParticipantBase):

    password: str | None = None # python 3.10부터 추가된 기능입니다.