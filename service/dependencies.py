from fastapi import Depends
from sqlalchemy.orm import Session

from service.db import get_db
from service.greeter.greeter_service import GreeterService


def get_greeter_service(db: Session = Depends(get_db)) -> GreeterService:
    return GreeterService(db)
