from sqlalchemy import Boolean, Column, String

from app.database import Base


class User(Base):
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    __hash__ = object.__hash__

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

    def __eq__(self, other):
        if isinstance(other, self):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
