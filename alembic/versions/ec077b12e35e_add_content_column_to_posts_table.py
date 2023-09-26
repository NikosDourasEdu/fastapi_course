"""add content column to posts table

Revision ID: ec077b12e35e
Revises: beff31799016
Create Date: 2023-09-25 22:50:31.001195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec077b12e35e'
down_revision: Union[str, None] = 'beff31799016'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
