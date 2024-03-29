"""added image to monster model

Revision ID: a6cceb672b80
Revises: 0d09cca47848
Create Date: 2024-02-27 10:26:23.002571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6cceb672b80'
down_revision = '0d09cca47848'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('monsters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('monsters', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
