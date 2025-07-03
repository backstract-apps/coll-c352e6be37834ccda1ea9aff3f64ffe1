from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(id: int, name: Annotated[str, Query(max_length=100)], login_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, id, name, login_details)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: Annotated[str, Query(max_length=100)], login_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name, login_details)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/todos/')
async def get_todos(db: Session = Depends(get_db)):
    try:
        return await service.get_todos(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/todos/id')
async def get_todos_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_todos_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/todos/')
async def post_todos(id: int, description: Annotated[str, Query(max_length=100)], completed: int, user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.post_todos(db, id, description, completed, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/todos/id/')
async def put_todos_id(id: int, description: Annotated[str, Query(max_length=100)], completed: int, user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.put_todos_id(db, id, description, completed, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/todos/id')
async def delete_todos_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_todos_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/file_storage')
async def post_file_storage(file: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_file_storage(db, file)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/join')
async def post_join(join_id: int, db: Session = Depends(get_db)):
    try:
        return await service.post_join(db, join_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

