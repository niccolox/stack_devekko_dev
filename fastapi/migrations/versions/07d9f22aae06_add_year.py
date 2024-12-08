"""add year

Revision ID: 07d9f22aae06
Revises: 2ea6d967f548
Create Date: 2024-12-08 05:05:21.208571

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '07d9f22aae06'
down_revision = '2ea6d967f548'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('stockprediction', sa.Column('year', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_stockprediction_year'), 'stockprediction', ['year'], unique=False)

def downgrade() -> None:
    op.drop_index(op.f('ix_stockprediction_year'), table_name='stockprediction')
    op.drop_column('stockprediction', 'year')
