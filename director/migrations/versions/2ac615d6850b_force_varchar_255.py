"""Force varchar 255

Revision ID: 2ac615d6850b
Revises: 063ff371f2da
Create Date: 2020-10-09 17:35:12.402690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2ac615d6850b"
down_revision = "063ff371f2da"
branch_labels = None
depends_on = None


def upgrade():
    """
    This migration is only useful for an existing Celery Director instance.
    """
    pass


def downgrade():
    pass
