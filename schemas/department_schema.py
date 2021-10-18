from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class DepartmentBase(BaseModel):
    id: Optional[UUID] = None
    name: str
    type: str
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):

    class Config:
        orm_mode = True
