import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, scoped_session

logger = logging.getLogger(__name__)

engine = create_engine(
    os.environ.get('DATABASE_URL'),
    encoding="utf-8",
    echo=False
)

session = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=True,
        bind=engine
    )
)
