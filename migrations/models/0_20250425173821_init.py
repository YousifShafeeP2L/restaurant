from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "restaurant" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(40) NOT NULL,
    "description" VARCHAR(40) NOT NULL,
    "image" VARCHAR(40) NOT NULL,
    "rating" DOUBLE PRECISION NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
