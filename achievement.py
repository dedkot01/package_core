from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.types import BigInteger

from . import config as conf
from .base import Base


class Achievement(Base):
    __tablename__ = "achievement"
    __table_args__ = {
        "schema": conf.default_schema,
    }

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    description: Mapped[str]
