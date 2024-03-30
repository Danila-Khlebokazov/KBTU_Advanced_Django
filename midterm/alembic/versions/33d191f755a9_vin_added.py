"""vin added

Revision ID: 33d191f755a9
Revises: e9fd6b7b3507
Create Date: 2024-03-09 17:11:58.142420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33d191f755a9'
down_revision: Union[str, None] = 'e9fd6b7b3507'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'vehicles', ['vin'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vehicles', type_='unique')
    # ### end Alembic commands ###