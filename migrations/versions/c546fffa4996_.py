"""empty message

Revision ID: c546fffa4996
Revises: 
Create Date: 2018-12-16 19:34:37.806196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c546fffa4996'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('tel', sa.String(length=11), nullable=False),
    sa.Column('password', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
