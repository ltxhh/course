"""empty message

Revision ID: 1794fbf2c6eb
Revises: 518f5bc7b97e
Create Date: 2022-04-06 14:57:35.592292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1794fbf2c6eb'
down_revision = '518f5bc7b97e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=500), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('q_id', sa.Integer(), nullable=True),
    sa.Column('reply', sa.Integer(), nullable=True),
    sa.Column('favorite', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.Column('sid', sa.Integer(), nullable=True),
    sa.Column('top', sa.Integer(), nullable=True),
    sa.Column('excellent', sa.Integer(), nullable=True),
    sa.Column('examine', sa.Integer(), nullable=True),
    sa.Column('favorite', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_type')
    op.drop_table('question')
    op.drop_table('comment')
    # ### end Alembic commands ###