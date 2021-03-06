"""empty message

Revision ID: d51d2e67b3da
Revises: 90af119ff762
Create Date: 2021-08-06 15:51:41.439216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd51d2e67b3da'
down_revision = '90af119ff762'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('series', sa.Column('archived', sa.Boolean(), nullable=True))
    op.execute("UPDATE series SET archived = false")
    op.alter_column("series", "archived", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('series', 'archived')
    # ### end Alembic commands ###
