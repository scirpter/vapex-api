import uvicorn
from fastapi import FastAPI
import asyncio
from db.server import start_db
from models.all import Product

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.post("/products")
async def create_product(product: Product) -> dict[str, str]:
    return product.model_dump()


async def main() -> None:
    await start_db()
    print("done")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
