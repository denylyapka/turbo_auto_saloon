import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.BuyListsRepository import BuyListsRepository
from app.models.dbModels.BuyLists.BuyListsEntity import BuyListsEntity as BuyList


async def get_list_by_id(list_id: int, session: AsyncSession) -> BuyList:
    repo_lists = BuyListsRepository(session)
    return await repo_lists.get_by_id(list_id=list_id)


async def get_all(session: AsyncSession) -> Any:
    repo_lists = BuyListsRepository(session)
    return await repo_lists.get_all()


async def get_all_by_type(list_type: str, session: AsyncSession) -> Any:
    repo_lists = BuyListsRepository(session)
    return await repo_lists.get_by_type(list_type=list_type)


async def create_buy_list(session: AsyncSession) -> BuyList:
    repo_lists = BuyListsRepository(session)

    buy_list = BuyList(
        type="type", products="products", datetime_create=datetime.datetime.now(), total_price=123456, total_discount=10
    )

    data = await repo_lists.create(buy_list=buy_list)

    return data


async def update_buy_list(buy_list: BuyList, session: AsyncSession) -> BuyList:
    repo_lists = BuyListsRepository(session)
    return await repo_lists.update(buy_list=buy_list)


async def delete_buy_list(list_id: int, session: AsyncSession) -> bool:
    repo_lists = BuyListsRepository(session)
    return await repo_lists.delete(list_id=list_id)
