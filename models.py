
# DB Connection

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import datetime
import pytz
class Participant(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email=Column(String(255))
    password=Column(String(255))
    age = Column(String(10))
    gender = Column(String(10))
    created_at=Column(
        datetime, default=lambda: datetime.now(pytz.timezone("Asia/Seoul"))
    )
    answers = relationship("Answer", back_populates='owner')

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question_id =Column(Integer)  # ForeignKey 제거, 정수 값으로 직접 저장
    chosen_answer = Column(String(10))
    owner_id = Column(Integer, ForeignKey('participants.id'))

    owner = relationship("Participant", back_populates='answers')
