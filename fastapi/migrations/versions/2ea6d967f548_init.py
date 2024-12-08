"""init

Revision ID: 2ea6d967f548
Revises: 
Create Date: 2024-12-08 04:42:55.812891

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '2ea6d967f548'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('stockprediction',
    sa.Column('ticker', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('forecast', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('stockprediction')
