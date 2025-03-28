from sqlalchemy import Column, Integer, String

from service.db import Base


class GreeterDB(Base):
    __tablename__ = "greeters"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    greet_msg = Column(String, nullable=False)
