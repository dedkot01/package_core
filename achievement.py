from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.types import BigInteger

from app_1.models import Base


class Achievement(Base):
    __tablename__ = "achievement"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    description: Mapped[str]
