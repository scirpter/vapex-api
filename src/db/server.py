import os
import urllib.parse
from tortoise import Tortoise


async def start_db() -> None:
    database_url: str = (
        "mysql://"
        + os.environ.get("POSTGRES_USER", "")
        + ":"
        + urllib.parse.quote_plus(os.environ.get("POSTGRES_PASSWORD", ""))
        + "@"
        + os.environ.get("POSTGRES_HOST", "")
        + ":"
        + os.environ.get("POSTGRES_PORT", "")
        + "/"
        + os.environ.get("POSTGRES_DATABASE", "")
        + "?maxsize=10"
    )
    await Tortoise.init(db_url=database_url, modules={"models": ["db.models"]})  # type: ignore
    await Tortoise.generate_schemas()
    print("connected to database")
