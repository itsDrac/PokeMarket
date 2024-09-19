"""Added Cart and M:M relationship with, User and Pokemon table.

Revision ID: 6a29b9e3607a
Revises: 0ac22aa1aacb
Create Date: 2024-09-07 19:38:13.652691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a29b9e3607a'
down_revision = '0ac22aa1aacb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('pokemons_carts',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart._id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon._id'], ),
    sa.PrimaryKeyConstraint('pokemon_id', 'cart_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemons_carts')
    op.drop_table('cart')
    # ### end Alembic commands ###