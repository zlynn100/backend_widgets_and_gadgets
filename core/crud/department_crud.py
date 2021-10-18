from sqlalchemy.orm import Session
from schemas import department_schema as dep_schema
from core.models import department_model as dep_model
from uuid import UUID

def get_department_by_id(db: Session, department_id: UUID):
    return db.query(dep_model.Department).filter(dep_model.Department.id == department_id).first()

def get_department_by_name(db: Session, department_name: UUID):
    return db.query(dep_model.Department).filter(dep_model.Department.name == department_name).first()

def get_departments(db: Session, limit: int = 2000):
    return db.query(dep_model.Department).limit(limit).all()

def create_department(db: Session, department: dep_schema.DepartmentCreate):
    dep = dep_model.Department(
        name=department.name,
        type=department.type,
        is_active=department.is_active,
    )
    db.add(dep)
    db.commit()
    db.refresh(dep)
    return dep

def update_department(db: Session, department_id: UUID) -> dep_schema.Department:
    return db.query