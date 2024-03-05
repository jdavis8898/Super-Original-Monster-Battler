"""added accuracy column to move model

Revision ID: 1134a14f7cdd
Revises: 4dee5321a1d7
Create Date: 2024-03-05 01:00:53.656186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1134a14f7cdd'
down_revision = '4dee5321a1d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('moves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('accuracy', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('moves', schema=None) as batch_op:
        batch_op.drop_column('accuracy')

    # ### end Alembic commands ###
