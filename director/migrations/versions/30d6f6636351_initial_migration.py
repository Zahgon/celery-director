"""Initial migration

Revision ID: 30d6f6636351
Revises: 
Create Date: 2020-02-07 18:34:41.680883

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types import UUIDType

from director.models.utils import JSONBType


# revision identifiers, used by Alembic.
revision = "30d6f6636351"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
