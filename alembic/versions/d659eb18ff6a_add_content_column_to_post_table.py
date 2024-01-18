"""add content column to post table

Revision ID: d659eb18ff6a
Revises: bca8ebeba212
Create Date: 2024-01-17 16:14:19.844713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd659eb18ff6a'
down_revision: Union[str, None] = 'bca8ebeba212'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column("content", sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
