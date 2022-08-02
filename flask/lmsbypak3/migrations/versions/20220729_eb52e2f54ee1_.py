"""empty message

Revision ID: eb52e2f54ee1
Revises: b8e69c0aa947
Create Date: 2022-07-29 19:19:53.585165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb52e2f54ee1'
down_revision = 'b8e69c0aa947'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students_assignments', sa.Column('received_grade', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students_assignments', 'received_grade')
    # ### end Alembic commands ###
