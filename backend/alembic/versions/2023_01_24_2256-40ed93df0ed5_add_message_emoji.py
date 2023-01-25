"""add message_emoji

Revision ID: 40ed93df0ed5
Revises: 8ba17b5f467a
Create Date: 2023-01-24 22:56:28.229408

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "40ed93df0ed5"
down_revision = "8ba17b5f467a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "message_emoji",
        sa.Column("message_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_date", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False
        ),
        sa.Column("emoji", sqlmodel.sql.sqltypes.AutoString(length=128), nullable=False),
        sa.ForeignKeyConstraint(["message_id"], ["message.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("message_id", "user_id", "emoji"),
    )
    op.create_index("ix_message_emoji__user_id__message_id", "message_emoji", ["user_id", "message_id"], unique=False)
    op.add_column("message", sa.Column("emojis", postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("message", "emojis")
    op.drop_index("ix_message_emoji__user_id__message_id", table_name="message_emoji")
    op.drop_table("message_emoji")
    # ### end Alembic commands ###
