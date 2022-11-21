"""init

Revision ID: e671b180f0f2
Revises: 
Create Date: 2022-11-21 08:48:27.211263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import MetaData

# revision identifiers, used by Alembic.
revision = 'e671b180f0f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_user_name', sa.String(length=200), nullable=False),
    sa.Column('second_user_name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=False),
    sa.Column('full_name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('hashed_password', sa.String(length=200), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('turn',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('throw',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('turn_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('value', sa.Enum('rock', 'paper', 'scissors', name='symbol', metadata=MetaData(), create_constraint=True), nullable=True),
    sa.ForeignKeyConstraint(['turn_id'], ['turn.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('throw')
    op.drop_table('turn')
    op.drop_table('user')
    op.drop_table('game')
    # ### end Alembic commands ###
