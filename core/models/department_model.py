from sqlalchemy import (Boolean, Column, String, DateTime, func)
from sqlalchemy.orm import relationship
from core.database import Base
from fastapi_utils.guid_type import GUID

class Department(Base):
    __tablename__ = 'departments'

    id = Column(GUID, primary_key=True, nullable=False,
                server_default='uuid_generate_v4()')
    name = Column(String, nullable=False, unique=True)
    type = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    updated_at = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    
    employees = relationship('Employee', back_populates='departments')