from fastapi import APIRouter, Depends, HTTPException
import crud
import dependencies
import schemas
from sqlalchemy.orm import Session
from typing import Union
router = APIRouter()

@router.post('/participant', response_model=schemas.Participant)
def create_participant(participant: schemas.ParticipantCreate, db: Session = Depends(dependencies.get_db)):
    db_participant= crud.create_participant(db, participant)
    return db_participant

# api/v1/participants/{user_id}
@router.get('/participant/{part_data}')
def get_participant_id(part_data: Union[int, str], db: Session = Depends(dependencies.get_db)):

    try: 
        part_data = int(part_data)
        if isinstance(part_data, int):
            db_part = crud.get_user_id(db, part_data)
    except:     
        if isinstance(part_data, str):
            db_part = crud.get_user_email(db, part_data)

    if db_part is None:
        raise HTTPException(status_code=404, detail='Participant Not Found')
    return db_part

# api/v1/users/email/{user_email}
# @router.get('/email/{user_email}')
# def get_user_email(user_email: str, db: Session = Depends(dependencies.get_db)):
#     db_user = crud.get_user_email(db, user_email)

#     if db_user is None:
#         raise HTTPException(status_code=404, detail='User Not Found')
#     return db_user
    

# api/v1/users/
@router.get('/participants')
def get_parts(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud.get_participants(db, skip, limit)

@router.put('/participant/{part_id}')
def update_part(part_id:int, part_update: schemas.ParticipantUpdate, db: Session = Depends(dependencies.get_db)):
    updated_part = crud.update_participants(db, part_id, part_update)

    if updated_part is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return updated_part

@router.delete('/participant/{part_id}')
def delete_part(part_id: int, db: Session = Depends(dependencies.get_db)):
    deleted_part = crud.delete_participant(db, part_id)
    
    if deleted_part is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return deleted_part