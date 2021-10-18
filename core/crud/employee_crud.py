from sqlalchemy.orm import Session
from core.models import employee_model as emp_model
from schemas import employee_schema as schema
from uuid import UUID

def get_employee_by_id(db: Session, employee_id: UUID):
    return db.query(emp_model.Employee).filter(emp_model.Employee.id == employee_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(emp_model.Employee).filter(emp_model.Employee.email == email).first()

def get_employees(db: Session, limit: int = 2000):
    return db.query(emp_model.Employee).limit(limit).all()

def create_employee(db: Session, employee: schema.EmployeeCreate):
    emp = emp_model.Employee(
        manager_id=employee.manager_id,
        department_id=employee.department_id,
        first_name=employee.first_name,
        last_name=employee.last_name,
        dob=employee.dob,
        email=employee.email,
        salary=employee.salary,
        phone=employee.phone,
        is_active=employee.is_active,
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp