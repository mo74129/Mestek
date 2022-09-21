"""Initial migration.

Revision ID: cc9b55f92db5
Revises: 
Create Date: 2022-07-29 16:54:24.026756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc9b55f92db5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('color_code', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('color_code'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('color_code', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('color_code'),
    sa.UniqueConstraint('name')
    )
    op.create_table('space',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(length=128), nullable=False),
    sa.Column('guidelines', sa.String(length=256), nullable=False),
    sa.Column('has_operator', sa.Boolean(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interval',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('calendar_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendar.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=False),
    sa.Column('guidelines', sa.String(length=256), nullable=False),
    sa.Column('has_operator', sa.Boolean(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('space_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['space_id'], ['space.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('space_id', sa.Integer(), nullable=True),
    sa.Column('tool_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['space_id'], ['space.id'], ),
    sa.ForeignKeyConstraint(['tool_id'], ['tool.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('space', 'tool', name='reservationtypes'), nullable=False),
    sa.Column('payment_status', sa.Enum('no_payment', 'down_payment', 'full_payment', name='paymenttypes'), nullable=False),
    sa.Column('transaction_num', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('calendar_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendar.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('image')
    op.drop_table('user')
    op.drop_table('tool')
    op.drop_table('interval')
    op.drop_table('space')
    op.drop_table('role')
    op.drop_table('category')
    op.drop_table('calendar')
    # ### end Alembic commands ###