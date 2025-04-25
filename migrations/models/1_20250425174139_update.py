from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "restaurant" ALTER COLUMN "description" DROP NOT NULL;
        ALTER TABLE "restaurant" ALTER COLUMN "image" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "restaurant" ALTER COLUMN "description" SET NOT NULL;
        ALTER TABLE "restaurant" ALTER COLUMN "image" SET NOT NULL;"""
