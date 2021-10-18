from sqlalchemy import (Boolean, Column, ForeignKey,
                        Float, String, DateTime, Numeric, func)
from sqlalchemy.orm import relationship
from core.database import Base
from fastapi_utils.guid_type import GUID


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(GUID, primary_key=True, nullable=False,
                server_default='uuid_generate_v4()')
    manager_id = Column(GUID, ForeignKey('employees.id'))
    department_id = Column(GUID, ForeignKey('departments.id'))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True)
    salary = Column(String)
    dob = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())

    departments = relationship('Department', back_populates='employees')
