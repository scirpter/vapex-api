import os
from tortoise import Tortoise
import ssl


async def start_db() -> None:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    await Tortoise.init(
        modules={"models": ["db.models"]},
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": os.environ.get("POSTGRES_DATABASE", "postgres"),
                        "host": os.environ.get("POSTGRES_HOST", "localhost"),
                        "password": os.environ.get("POSTGRES_PASSWORD", "postgres"),
                        "port": os.environ.get("POSTGRES_PORT", "5432"),
                        "user": os.environ.get("POSTGRES_USER", "postgres"),
                        "ssl": ctx,
                    },
                }
            },
            "apps": {
                "models": {
                    "models": ["db.models"],
                    "default_connection": "default",
                }
            },
        },
    )  # type: ignore
    await Tortoise.generate_schemas()
