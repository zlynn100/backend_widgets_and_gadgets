from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class EmployeeBase(BaseModel):
    id: Optional[UUID] = None
    first_name: str
    last_name: str
    is_active: bool
    dob: datetime
    email: str
    manager_id: Optional[UUID] = None
    department_id: Optional[UUID] = None
    phone: Optional[str] = None
    salary: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    
    class Config:
        orm_mode = True
