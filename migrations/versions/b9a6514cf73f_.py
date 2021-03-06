"""empty message

Revision ID: b9a6514cf73f
Revises: eaf429afa5d4
Create Date: 2021-06-14 17:01:33.969876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a6514cf73f'
down_revision = 'eaf429afa5d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_association_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'comment_association', ['comment_association_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'comment_association_id')
    # ### end Alembic commands ###
