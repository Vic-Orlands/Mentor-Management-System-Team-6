"""association tables not inheriting from Abstract base.

Revision ID: 83195a444300
Revises: bbe28d4a49cd
Create Date: 2023-05-02 17:51:32.775491

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '83195a444300'
down_revision = 'bbe28d4a49cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('participant_conversation_association', 'updated')
    op.drop_column('participant_conversation_association', 'created')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('participant_conversation_association', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('participant_conversation_association', sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
