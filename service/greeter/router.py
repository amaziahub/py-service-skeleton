import logging

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from service.db import get_db
from service.greeter import greeter_service
from service.greeter.schemas.greet import Greeter

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
def post_greet(greeter: Greeter, db: Session = Depends(get_db)):
    saved_greeter = greeter_service.save_greet(db, greeter)
    logger.info(f"Received greet: {saved_greeter.greet_msg} from {saved_greeter.name}")
