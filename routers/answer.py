from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import dependencies
import crud
import schemas

router = APIRouter()

@router.get('/answer/{answer_id}')
def get_answer(answer_id: int, db: Session = Depends(dependencies.get_db)):
    answer = crud.get_answer(db, answer_id)

    if answer is None:
        raise HTTPException(status_code=404, detaul='Answer not found')
    return answer

# items => skip, limit
@router.get('/answers')    
def get_answers(skip: int=0, limit: int=10, db: Session = Depends(dependencies.get_db)):
    answers = crud.get_answers(db, skip, limit)
    return answers # []

@router.post('/answer')
def create_answer(create_answer: schemas.AnswerCreate, owner_id: int, db: Session = Depends(dependencies.get_db)):
    answer = crud.create_answer(db, create_answer, owner_id)
    return answer

@router.put('/answer/{answer_id}')
def update_answer(answer_id: int, answer_update: schemas.AnswerUpdate, db: Session = Depends(dependencies.get_db)):
    answer = crud.update_answer(db, answer_id, answer_update)

    if answer is None:
        raise HTTPException(status_code=404, default='Answer not found')
    return answer 

@router.delete('/answer/{answer_id}')
def delete_answer(answer_id: int, db: Session = Depends(dependencies.get_db)):
    is_success = crud.delete_answer(db, answer_id)

    if not is_success:
        raise HTTPException(status_code=404, detaul='Answer not found')
    return {"msg":"Success delete item"}

@router.get('/answer/results/{owner_id}')
def results(owner_id:int,db:Session=Depends(dependencies.get_db)):
    