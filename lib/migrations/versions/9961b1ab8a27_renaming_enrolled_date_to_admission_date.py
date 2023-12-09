"""Renaming enrolled_date to admission_date

Revision ID: 9961b1ab8a27
Revises: 791279dd0760
Create Date: 2023-12-10 00:20:00.109072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9961b1ab8a27'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'enrolled_date', new_column_name='admission_date')


def downgrade() -> None:
    op.alter_column('students', 'admission_date', new_column_name='enrolled_date')
