from sqlalchemy import insert, select

from slack_bot.models.user import User
from slack_bot.database.db import session_scope


def create_user(user_id, username):
    with session_scope() as session:
        session.execute(
            insert(User), {
                'id': user_id,
                'username': username,
            }
        )


def get_user(user_id: int):
    stmt = select(User).where(User.id == user_id)
    with session_scope() as session:
        user = session.scalars(stmt).one_or_none()
    return user
