"""empty message

Revision ID: 3f1e73110198
Revises: 07ea68c170a2
Create Date: 2023-04-07 02:34:08.422700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f1e73110198'
down_revision = '07ea68c170a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('latest_question_ts', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'latest_question_ts')
    # ### end Alembic commands ###