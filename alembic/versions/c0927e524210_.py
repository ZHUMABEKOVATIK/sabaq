"""empty message

Revision ID: c0927e524210
Revises: 5fe3adc2b499
Create Date: 2026-05-06 18:04:29.214844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0927e524210'
down_revision: Union[str, Sequence[str], None] = '5fe3adc2b499'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
