from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from slack_bot.config import get_db_uri
from sqlalchemy.exc import IntegrityError

engine = create_engine(
    get_db_uri(),
)
SessionLocal = scoped_session(
    sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)
)

Base = declarative_base()


@contextmanager
def session_scope():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except IntegrityError:
        session.rollback()
        pass
    finally:
        session.close()
