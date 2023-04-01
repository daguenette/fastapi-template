"""add taxes table

Revision ID: ffe93efeb770
Revises: dfa74266eef3
Create Date: 2023-03-30 16:03:33.807385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffe93efeb770'
down_revision = 'dfa74266eef3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('taxes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('salary_income', sa.Integer(), nullable=True),
    sa.Column('salary_hours', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_taxes_email'), 'taxes', ['email'], unique=True)
    op.create_index(op.f('ix_taxes_id'), 'taxes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_taxes_id'), table_name='taxes')
    op.drop_index(op.f('ix_taxes_email'), table_name='taxes')
    op.drop_table('taxes')
    # ### end Alembic commands ###