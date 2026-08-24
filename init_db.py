from app.db.database import Base
from app.db.database import engine

from app.models.analysis import Analysis


def initialize_database():

    Base.metadata.create_all(
        bind=engine
    )