from typing import List
from fastapi import APIRouter, Depends, HTTPException
from schemas import employee_schema as emp_schema
from core.crud import employee_crud
from sqlalchemy.orm import Session
from core.database import get_db
from uuid import UUID
import re

router = APIRouter(
    prefix='/employees',
    tags=['employees'],
    dependencies=[Depends(get_db)]
)


@router.post('/', response_model=emp_schema.Employee)
def create_employee(employee: emp_schema.EmployeeCreate, db: Session = Depends(get_db)):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(email_regex, employee.email):
        raise HTTPException(status_code=400, detail='Invalid email format passed.')
    
    emp = employee_crud.get_employee_by_email(
        db, email=employee.email)
    if emp:
        raise HTTPException(
            status_code=400, detail='Email is already in use by another employee.')
    
    return employee_crud.create_employee(db=db, employee=employee)


@router.get('/', response_model=List[emp_schema.Employee])
def read_employees(limit: int = 2000, db: Session = Depends(get_db)):
    employees = employee_crud.get_employees(db=db, limit=limit)
    return employees


@router.get('/{employee_id}', response_model=emp_schema.Employee)
def read_employee(employee_id: UUID, db: Session = Depends(get_db)):
    emp = employee_crud.get_employee_by_id(db=db, employee_id=employee_id)
    if emp is None:
        raise HTTPException(status_code=404, detail='Employee not found.')
    return emp
