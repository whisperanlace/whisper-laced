import os
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

url = os.environ.get("DATABASE_URL", "")
if url:
    config.set_main_option("sqlalchemy.url", url)

# ORM Base
from backend.db import Base  # noqa

# --- Import models in dependency-safe order ---
import backend.models.user  # users must load first  # noqa
import backend.models.base  # noqa
import backend.models.toggle  # noqa
import backend.models.feature_toggle  # noqa
import backend.models.system_flag  # noqa
import backend.models.tier  # noqa
import backend.models.premium_model  # noqa
import backend.models.settings  # noqa
import backend.models.lora  # noqa
import backend.models.avatar  # noqa
import backend.models.upload  # noqa
import backend.models.media  # noqa
import backend.models.video  # noqa
import backend.models.whisper_model  # noqa
import backend.models.history  # noqa
import backend.models.metrics  # noqa
import backend.models.analytics  # noqa
import backend.models.community  # noqa
import backend.models.lounge  # noqa
import backend.models.post  # noqa
import backend.models.comment  # noqa
import backend.models.reaction  # noqa
import backend.models.invite  # noqa
import backend.models.motion  # noqa
import backend.models.moderation  # noqa
import backend.models.report  # noqa
import backend.models.editor  # noqa
import backend.models.roles  # noqa
import backend.models.audit  # noqa
import backend.models.tokens  # noqa
# ----------------------------------------------

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
