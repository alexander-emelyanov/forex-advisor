"""empty message

Revision ID: 430ebbed113
Revises: 56d72bc16f5
Create Date: 2015-04-10 03:32:17.164390

"""

# revision identifiers, used by Alembic.
revision = '430ebbed113'
down_revision = '56d72bc16f5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # commands auto generated by Alembic - please adjust! ###
    op.create_table('market',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('symbol', sa.Column('code', sa.String(), nullable=False))
    op.add_column('symbol', sa.Column('market_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'symbol', 'market', ['market_id'], ['id'])
    # end Alembic commands ###


def downgrade():
    # commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'symbol', type_='foreignkey')
    op.drop_column('symbol', 'market_id')
    op.drop_column('symbol', 'code')
    op.drop_table('market')
    # end Alembic commands ###
