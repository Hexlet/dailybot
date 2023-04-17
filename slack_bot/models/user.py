from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base
from slack_bot.models.report import Report


class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str]
    latest_question_ts: Mapped[str | None]
    report: Mapped[List["Report"] | None] = relationship(
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'User {self.id} {self.username}'
