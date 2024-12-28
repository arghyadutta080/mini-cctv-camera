"""Updated FaceDetection model

Revision ID: 79f7bea8251a
Revises: 
Create Date: 2024-12-29 00:38:57.936266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79f7bea8251a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('face_detection', schema=None) as batch_op:
        batch_op.add_column(sa.Column('face_count', sa.Integer(), nullable=True))
        batch_op.drop_column('face_coordinates')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('face_detection', schema=None) as batch_op:
        batch_op.add_column(sa.Column('face_coordinates', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('face_count')

    # ### end Alembic commands ###
