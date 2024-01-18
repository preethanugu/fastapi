"""create posts table

Revision ID: bca8ebeba212
Revises: 
Create Date: 2024-01-16 12:19:24.970116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bca8ebeba212'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable =False, primary_key= True),
    sa.Column("title", sa.String(), nullable = False))

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
