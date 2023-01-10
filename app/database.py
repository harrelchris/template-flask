"""
This module contains the SQLAlchemy database connection and a Base model.

The environment should include a variable called `DATABASE_URL` which
conforms to the SQLAlchemy URL schema as described here:
https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls

The Base model includes an auto-incrementing primary key column called `id`.

The Base model includes automatic `created` and `modified` columns which will
record when records are created and modified per the database server time.

The Base model includes all features from sqlalchemy_mixins.AllFeaturesMixin
as documented here: https://github.com/absent1706/sqlalchemy-mixins.

Example:
    from sqlalchemy import Column, String
    from .database import Base
    class MyMode(Base):
        name = Column(String(120))
"""
from sqlalchemy import Column, DateTime, Integer, MetaData, create_engine, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy_mixins import AllFeaturesMixin

from app.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=True))
metadata = MetaData()


class BaseModel(AllFeaturesMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=False), server_default=func.now())
    modified = Column(DateTime(timezone=False), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


BaseModel.set_session(session)
Base = declarative_base(metadata=metadata, cls=BaseModel)
