from models import Participant, Answer
from schemas import ParticipantCreate, ParticipantUpdate, AnswerCreate, AnswerUpdate
from sqlalchemy.orm import Session
import bcrypt # pip insall bcrypt
#participant crud
def create_participant(db:Session,participant:ParticipantCreate):
    hashed_password= bcrypt.hashpw(participant
        .password.encode('utf-8'), bcrypt.gensalt())
    db_participant = Participant(
        email=Participant.email,
        name=Participant.name,
        age=Participant.age,
        gender=Participant.gender,
        password=hashed_password
        )
    db.add(db_participant)
    db.commit()
    return db_participant

def get_participant_id(db: Session, id: int):
    return db.query(Participant).filter(Participant.id == id).first()

# participant의 email값을 기반으로 데이터를 찾는다.
def get_participant_email(db: Session, email):
    return db.query(Participant).filter(Participant.email == email).first()

def get_participants(db: Session, skip: int=0, limit: int = 10):
    return db.query(Participant).offset(skip).limit(limit).all()

def update_participants(db:Session,id:int,participantUpdate:ParticipantUpdate):
    db_participant=db.query(Participant).filter(Participant.id == id).first()
    if not db_participant:
        return None
    
    participant_data=participantUpdate.dict()
    for key,value in participant_data.items():
        setattr(db_participant, key, value)
    
    db.commit()
    db.refresh(db_participant)
    
    return db_participant

def delete_participant(db: Session, id: int):
    db_participant = db.query(Participant).filter(Participant.id == id).first()

    if not db_participant:
        return None
    
    db.delete(db_participant)
    db.commit()
    return db_participant

#Answer CRUD
def get_answer(db:Session,answer_id:int):
    return db.query(Answer).filter(Answer.id == answer_id).first()

def get_answers(db: Session, skip: int = 0, limit: int = 10): # 전체 answer 데이터 조회 (Limit: 10~100)
    return db.query(Answer).offset(skip).limit(limit).all()

def create_answer(db:Session,answer:AnswerCreate,owner_id:int):
    db_answer=Answer(**answer.dict(),owner_id=owner_id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)

    return db_answer

def update_answer(db:Session,id:int,answer_update:AnswerUpdate):
    db_answer=db.query(Answer).filter(Answer.id==id).first()
    if not db_answer:
        return None
    for key,value in answer_update.dict().items():
        setattr(db_answer, key, value)

    db.commit()
    db.refresh(db_answer)
    return db_answer

def delete_answer(db: Session, id: int): # 하나의 데이터 삭제 {item_id}
    db_answer = db.query(Answer).filter(Answer.id == id).first()
    if not db_answer:
        return None

    db.delete(db_answer)
    db.commit()

    return True