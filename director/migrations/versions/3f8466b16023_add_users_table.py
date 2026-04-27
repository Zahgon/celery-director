"""Add users table

Revision ID: 3f8466b16023
Revises: 05cf96d6fcae
Create Date: 2020-07-15 16:45:02.209593

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils.types import UUIDType


# revision identifiers, used by Alembic.
revision = "3f8466b16023"
down_revision = "05cf96d6fcae"
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
