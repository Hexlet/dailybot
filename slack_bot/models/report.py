import enum
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from slack_bot.dialog.interactive import EDIT_BUTTON
from database.db import Base


class ReportStatus(enum.Enum):
    not_started = 0
    progress = 1
    plans = 2
    complete = 3


class Report(Base):
    __tablename__ = 'reports'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[ReportStatus]
    progress: Mapped[str | None]
    plans: Mapped[str | None]
    blockers: Mapped[str | None]
    message_timestamp: Mapped[str | None]
    report_timestamp: Mapped[str | None]

    def __str__(self):
        return f'User: {self.user_id} \
            status: {self.status} \
            progress: {self.progress} \
            plans: {self.plans} \
            blockers: {self.blockers}'

    @property
    def info(self):
        return self.progress, self.plans, self.blockers

    def is_newer_message(self, user_message_ts):
        return self.message_timestamp < user_message_ts

    def is_not_started(self):
        return self.status == ReportStatus.not_started

    def is_completed(self):
        return self.status == ReportStatus.complete

    def is_in_progress(self):
        return self.status == ReportStatus.progress

    def is_in_plans(self):
        return self.status == ReportStatus.plans

    def get_message(self):
        if self.status == ReportStatus.progress:
            message = 'Today plans?'
        elif self.status == ReportStatus.plans:
            message = 'Blockers?'
        elif self.status == ReportStatus.complete:
            message = EDIT_BUTTON
        return message
