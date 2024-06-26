"""vin added

Revision ID: e9fd6b7b3507
Revises: f3711a58dc3a
Create Date: 2024-03-09 17:11:01.621782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9fd6b7b3507'
down_revision: Union[str, None] = 'f3711a58dc3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('vin', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicles', 'vin')
    # ### end Alembic commands ###
