from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "9e803aa66b58"
down_revision: Union[str, None] = "35942731785d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # backfill any NULLs first so NOT NULL can be enforced safely
    op.execute("UPDATE users SET created_at = now() WHERE created_at IS NULL;")
    op.execute("UPDATE users SET updated_at = now() WHERE updated_at IS NULL;")

    # set defaults + NOT NULL
    op.alter_column(
        "users", "created_at",
        existing_type=sa.DateTime(timezone=True),
        server_default=sa.text("now()"),
        nullable=False
    )
    op.alter_column(
        "users", "updated_at",
        existing_type=sa.DateTime(timezone=True),
        server_default=sa.text("now()"),
        nullable=False
    )

def downgrade() -> None:
    op.alter_column(
        "users", "updated_at",
        existing_type=sa.DateTime(timezone=True),
        server_default=None,
        nullable=True
    )
    op.alter_column(
        "users", "created_at",
        existing_type=sa.DateTime(timezone=True),
        server_default=None,
        nullable=True
    )
