"""added miniLM_embedding column to message

Revision ID: 023548d474f7
Revises: ba61fe17fb6e
Create Date: 2023-01-08 11:06:25.613290

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "023548d474f7"
down_revision = "ba61fe17fb6e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("message", sa.Column("miniLM_embedding", sa.ARRAY(sa.Float()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("message", "miniLM_embedding")
    # ### end Alembic commands ###
