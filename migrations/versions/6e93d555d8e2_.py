"""empty message

Revision ID: 6e93d555d8e2
Revises: 
Create Date: 2024-05-06 01:16:19.674260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e93d555d8e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    
    with op.batch_alter_table('list_item', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('user_top_10', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('user_top_5_dir', schema=None) as batch_op:
        batch_op.add_column(sa.Column('director_image_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('director_id')

    with op.batch_alter_table('user_wish_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('movie_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('wishlist_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_wish_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('wishlist_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'movie', ['wishlist_id'], ['id'])
        batch_op.drop_column('movie_id')

    with op.batch_alter_table('user_top_5_dir', schema=None) as batch_op:
        batch_op.add_column(sa.Column('director_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'movie', ['director_id'], ['id'])
        batch_op.drop_column('director_image_id')

    with op.batch_alter_table('user_top_10', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'movie', ['movie_id'], ['id'])

    with op.batch_alter_table('list_item', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'movie', ['movie_id'], ['id'])

    op.create_table('movie',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('total_rating', sa.INTEGER(), nullable=True),
    sa.Column('num_ratings', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_rating',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('movie_id', sa.INTEGER(), nullable=False),
    sa.Column('rating', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'movie_id', name='_user_movie_uc')
    )
    # ### end Alembic commands ###