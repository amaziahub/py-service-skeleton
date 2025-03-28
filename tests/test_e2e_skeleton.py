from service.db import models
from service.db.db import engine

models.Base.metadata.create_all(bind=engine)


def test_is_healthy(app):
    assert app.is_healthy()
