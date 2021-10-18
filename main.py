from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from core.models import employee_model
from core.database import engine

from v1.routers import employees, departments

employee_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(employees.router)
app.include_router(departments.router)
