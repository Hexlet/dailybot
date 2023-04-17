from sqlalchemy import insert, select, update

from slack_bot.models.report import Report, ReportStatus
from slack_bot.database.db import session_scope

STOP_WORDS = ['no', 'none', 'нет', '-']


def create_user_report(user_id, message_ts):
    with session_scope() as session:
        report = session.execute(
            insert(Report).values(
                user_id=user_id,
                status=ReportStatus.not_started,
                message_timestamp=message_ts,
            )
        )
    return report


def get_latest_report(user_id) -> Report:
    stmt = select(Report).where(
        Report.user_id == user_id
    ).order_by(
        Report.message_timestamp.desc()
    )
    with session_scope() as session:
        report = session.scalar(stmt)
    return report


def is_blockers(message_content):
    return message_content in STOP_WORDS


def save_report_part(report, message_content):
    with session_scope() as session:
        match report.status:
            case ReportStatus.not_started:
                return session.execute(
                    update(Report).where(Report.id == report.id).returning(Report), {
                        'id': report.id,
                        'progress': message_content,
                        'status': ReportStatus.progress,
                    }
                ).scalar()
            case ReportStatus.progress:
                return session.execute(
                    update(Report).where(Report.id == report.id).returning(Report), {
                        'id': report.id,
                        'plans': message_content,
                        'status': ReportStatus.plans,
                    }
                ).scalar()
            case ReportStatus.plans:
                return session.execute(
                    update(Report).where(Report.id == report.id).returning(Report), {
                        'id': report.id,
                        'blockers': None if is_blockers(message_content) else message_content,
                        'status': ReportStatus.complete,
                    }
                ).scalar()


def update_timestamp(report, ts, type):
    with session_scope() as session:
        if type == 'question':
            session.execute(
                update(Report).where(Report.id == report.id), {
                    'id': report.id,
                    'message_timestamp': ts,
                }
            )
        else:
            session.execute(
                update(Report).where(Report.id == report.id), {
                    'id': report.id,
                    'report_timestamp': ts,
                }
            )
