import logging

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from service.db import greeter_persistence
from service.db import schemas
from service.db.db import get_db

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
def post_greet(greeter: schemas.Greeter, db: Session = Depends(get_db)):
    saved_greeter = greeter_persistence.save_greet(db, greeter)
    logger.info(f"Received greet: {saved_greeter.greet_msg} from {saved_greeter.name}")
