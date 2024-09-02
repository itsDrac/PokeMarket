"""Pokemon Table and Category table with many to many rel.

Revision ID: 9bcabe3fbb43
Revises: 4dd1b340abd4
Create Date: 2024-08-28 18:24:55.294159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bcabe3fbb43'
down_revision = '4dd1b340abd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('_id')
    )
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_category_name'), ['name'], unique=True)

    op.create_table('pokemon',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.Column('imgUrl', sa.String(length=60), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('quantity', sa.SmallInteger(), nullable=False),
    sa.Column('inStock', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('pokemon_type',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category._id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon._id'], ),
    sa.PrimaryKeyConstraint('pokemon_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon_type')
    op.drop_table('pokemon')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_category_name'))

    op.drop_table('category')
    # ### end Alembic commands ###
