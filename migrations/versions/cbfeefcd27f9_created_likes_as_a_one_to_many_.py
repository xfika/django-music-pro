"""Created likes as a one to many polymorphic

Revision ID: cbfeefcd27f9
Revises: b9a6514cf73f
Create Date: 2021-06-30 19:06:34.634941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbfeefcd27f9'
down_revision = 'b9a6514cf73f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('like_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dicriminator', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('like_id', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('association_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['association_id'], ['like_association.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('like_id')
    )
    op.add_column('albums', sa.Column('like_association_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'albums', 'like_association', ['like_association_id'], ['id'])
    op.drop_column('albums', 'likes')
    op.add_column('comments', sa.Column('like_association_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'like_association', ['like_association_id'], ['id'])
    op.add_column('media', sa.Column('like_association_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'media', 'like_association', ['like_association_id'], ['id'])
    op.drop_column('media', 'likes')
    op.add_column('playlists', sa.Column('like_association_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'playlists', 'like_association', ['like_association_id'], ['id'])
    op.drop_column('playlists', 'likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playlists', sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'playlists', type_='foreignkey')
    op.drop_column('playlists', 'like_association_id')
    op.add_column('media', sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'media', type_='foreignkey')
    op.drop_column('media', 'like_association_id')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'like_association_id')
    op.add_column('albums', sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'albums', type_='foreignkey')
    op.drop_column('albums', 'like_association_id')
    op.drop_table('likes')
    op.drop_table('like_association')
    # ### end Alembic commands ###
