from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.buy_lists import BuyListService
from app.services.test_services.user_buy_lists import UserBuyListsService

from app.models.dtoModels.BuyListsDTO import BuyListsDTO, ProductDTO

from app.models.dbModels.BuyLists.BuyListsEntity import BuyListsEntity
from app.models.dbModels.UserBuyLists.UserBuyListsEntity import UserBuyListsEntity


router = APIRouter()


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.get_by_id(self=repo, list_id=id)
    return data

@router.get("/")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.get_all(self=repo)
    return data

@router.get("/type/{list_type}")
async def get_by_type(list_type: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.get_all_by_type(self=repo, list_type=list_type)
    return data

@router.post("/add_buy_list")
async def add_buy_list(
    buy_list_dto: BuyListsDTO, 
    session: AsyncSession = Depends(fastapi_get_db)
):
    service = BuyListService(session)
    
    # Преобразуем список ProductDTO в список словарей
    products_data = [
        {
            "type_prod": p.type_prod,
            "id_prod": p.id_prod,
            "quantity": p.quantity
        } for p in buy_list_dto.products
    ]
    
    # Создаем Entity объект
    buy_list = BuyListsEntity(
        type=buy_list_dto.type,
        products=products_data,  # ARRAY(JSON) примет список словарей
        total_price=buy_list_dto.total_price,
        total_discount=buy_list_dto.total_discount
    )

    response_create_bl = await service.create(buy_list)

    user_buy_list_data = UserBuyListsEntity(
        user_id=buy_list_dto.user_id,
        buy_list_id=response_create_bl["id"]
    )

    service_ubl = UserBuyListsService(session)
    response_create_ubl = await service_ubl.create(user_buy_list=user_buy_list_data)
    
    return {
        "buy_list": response_create_bl,
        "user_buy_list": response_create_ubl
    }

@router.delete("/{id}")
async def delete(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await repo.delete(list_id=id)
    return data


@router.put("/{id}")
async def update(id: int, buy_list_dto: BuyListsDTO, session: AsyncSession = Depends(fastapi_get_db)):
    service = BuyListService(session)
    
    # Преобразуем DTO в Entity
    products_data = [
        {
            "type_prod": p.type_prod,
            "id_prod": p.id_prod,
            "quantity": p.quantity
        } for p in buy_list_dto.products
    ]
    
    buy_list_entity = BuyListsEntity(
        id=id,  # Важно передать ID для обновления
        type=buy_list_dto.type,
        products=products_data,
        total_price=buy_list_dto.total_price,
        total_discount=buy_list_dto.total_discount
    )
    
    return await service.update(buy_list_entity)


@router.get("/products/{buy_list_id}")
async def get_products_by_buy_list_id(buy_list_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    service = BuyListService(session)
    data = await service.get_products_by_buy_list_id(buy_list_id=buy_list_id)
    return data

@router.post("/remove_product")
async def delete_product(buy_list_id: int, product_index: int, session: AsyncSession = Depends(fastapi_get_db)):
    service = BuyListService(session)
    data = await service.delete_product(buy_list_id=buy_list_id, product_index=product_index)
    return data