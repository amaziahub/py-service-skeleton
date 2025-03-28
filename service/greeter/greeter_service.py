from sqlalchemy.orm import Session

from service.greeter.models.greet import GreeterDB
from service.greeter.schemas.greet import Greeter


class GreeterService:
    def __init__(self, db: Session):
        self.db = db

    def save_greet(self, greeter: Greeter) -> GreeterDB:
        db_greeter = GreeterDB(**greeter.model_dump())
        self.db.add(db_greeter)
        self.db.commit()
        self.db.refresh(db_greeter)
        return db_greeter

    def get_greeter_by_id(self, greeter_id: int):
        return self.db.query(GreeterDB).filter(GreeterDB.id == greeter_id).first()
