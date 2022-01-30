"""create user table

Revision ID: 81445603f267
Revises: 
Create Date: 2022-01-30 14:03:06.790912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81445603f267'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True)
    )

def downgrade():
    op.drop_table('user')
