from alembic import context
from sqlalchemy import engine_from_config, pool

from app.config import settings
from app.domain import Base

config = context.config

section = config.config_ini_section
config.set_section_option(section, "POSTGRES_USER", settings.POSTGRES_USER)
config.set_section_option(section, "POSTGRES_PASSWORD", settings.POSTGRES_PASSWORD)
config.set_section_option(section, "POSTGRES_DB", settings.POSTGRES_DB)
config.set_section_option(section, "POSTGRES_SERVER", settings.POSTGRES_SERVER)
config.set_section_option(section, "POSTGRES_APPLICATION_NAME", settings.POSTGRES_APPLICATION_NAME)
config.set_section_option(section, "POSTGRES_PORT", settings.POSTGRES_PORT)

target_metadata = Base.metadata


def online_connection():
    connectable = context.config.attributes("connection", None)

    if connectable is None:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool
        )

    with connectable.connect() as con:
        context.configure(
            connection=con,
            compare_type=True
        )
        yield con


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
