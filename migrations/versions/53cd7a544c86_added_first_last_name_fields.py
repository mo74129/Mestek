"""Added first & last name fields

Revision ID: 53cd7a544c86
Revises: 84b334b2c5ea
Create Date: 2022-07-20 16:53:41.605548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53cd7a544c86'
down_revision = '84b334b2c5ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
