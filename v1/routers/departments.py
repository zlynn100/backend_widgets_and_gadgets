from typing import List
from fastapi import APIRouter, Depends, HTTPException
from schemas import department_schema as dep_schema
from core.crud import department_crud
from sqlalchemy.orm import Session
from core.database import get_db
from uuid import UUID

router = APIRouter(
    prefix='/departments',
    tags=['departments'],
    dependencies=[Depends(get_db)]
)

@router.post('/', response_model=dep_schema.Department)
def create_department(department: dep_schema.DepartmentCreate, db: Session = Depends(get_db)):
    dep = department_crud.get_department_by_name(db, department_name=department.name)
    if dep:
        raise HTTPException(status_code=400, detail='Department name is already in use.')
    
    return department_crud.create_department(db=db, department=department)

@router.get('/', response_model=List[dep_schema.Department])
def read_departments(limit: int = 2000, db: Session = Depends(get_db)):
    return department_crud.get_departments(db=db, limit=limit)