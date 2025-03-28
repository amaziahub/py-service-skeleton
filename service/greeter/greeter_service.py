from sqlalchemy.orm import Session

from service.greeter.models.greet import GreeterDB
from service.greeter.schemas.greet import Greeter


def save_greet(db: Session, greeter: Greeter):
    db_greeter = GreeterDB(**greeter.model_dump())
    db.add(db_greeter)
    db.commit()
    db.refresh(db_greeter)
    return db_greeter


def get_greeter_by_id(db: Session, greeter_id: int):
    return db.query(GreeterDB).filter(GreeterDB.id == greeter_id).first()
