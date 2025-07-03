from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db

from app.services.test_services.car import CarEntityService, EngineService, ChassisService, InteriorService, DimensionsService
from app.models.dbModels.Cars.Entities.CarEntity import CarEntity
from app.models.dbModels.Cars.Entities.CarChassis import CarChassis
from app.models.dbModels.Cars.Entities.CarEngine import CarEngine
from app.models.dbModels.Cars.Entities.CarDimensions import CarDimensions
from app.models.dbModels.Cars.Entities.CarInterior import CarInterior

from app.models.dtoModels.CarTotalDTO import CarTotalDTO
from app.models.dtoModels.ChassisDTO import ChassisDTO
from app.models.dtoModels.EngineDTO import EngineDTO
from app.models.dtoModels.DimensionsDTO import DimensionsDTO
from app.models.dtoModels.InteriorDTO import InteriorDTO

router = APIRouter()


# CarEntityService

@router.post("/car")
async def create(car_dto: CarTotalDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CarEntityService(session)

    chassis_data = CarChassis(
        expenditure=car_dto.expenditure,
        overclocking=car_dto.overclocking,
        quantity_places=car_dto.quantity_places,
        volume_trunk=car_dto.volume_trunk
    )

    engine_data = CarEngine(
        turbine=car_dto.turbine,
        engine_type=car_dto.engine_type,
        engine_cylinders=car_dto.engine_cylinders,
        volume_engine=car_dto.volume_engine,
        power_hp=car_dto.power_hp,
        power_nm=car_dto.power_nm
    )

    dimensions_data = CarDimensions(
        clearance=car_dto.clearance,
        width=car_dto.width,
        height=car_dto.height,
        length=car_dto.length,
        wheelbase=car_dto.wheelbase,
        front_track=car_dto.front_track,
        rear_track=car_dto.rear_track
    )

    interior_data = CarInterior(
        conditioner=car_dto.conditioner,
        safety=car_dto.safety,
        steering_control_material=car_dto.steering_control_material,
        steering_control_side=car_dto.steering_control_side,
        steering_control_type_of_amplifier=car_dto.steering_control_type_of_amplifier,
        climate=car_dto.climate,
        wheel_diameter=car_dto.wheel_diameter,
        anti_theft=car_dto.anti_theft,
        help_driving=car_dto.help_driving,
        salon_material=car_dto.salon_material,
        salon_hatch=car_dto.salon_hatch,
        salon_color=car_dto.salon_color,
        heated=car_dto.heated,
        electric=car_dto.electric,
        head_lights_type=car_dto.head_lights_type,
        head_lights_washers=car_dto.head_lights_washers,
        multumedia=car_dto.multumedia,
        quantity_speaker=car_dto.quantity_speaker,
        subwoofer=car_dto.subwoofer,
        memory=car_dto.memory
    )

    response_create_car_chassis = await ChassisService.create(self=repo, chassis=chassis_data)
    response_create_car_engine = await EngineService.create(self=repo, engine=engine_data)
    response_create_car_dimensions = await DimensionsService.create(self=repo, dimensions=dimensions_data)
    response_create_car_interior = await InteriorService.create(self=repo, interior=interior_data)

    car_data = CarEntity(
        vin_id=car_dto.vin_id,
        country_manufacturer=car_dto.country_manufacturer,
        description=car_dto.description,
        brand=car_dto.brand,
        model=car_dto.model,
        year_of_release=car_dto.year_of_release,
        photos=car_dto.photos,
        mileage=car_dto.mileage,
        gear_box=car_dto.gear_box,
        drive=car_dto.drive,
        condition=car_dto.condition,
        body_type=car_dto.body_type,
        color=car_dto.color,
        engine_id=response_create_car_engine.id,
        chassis_id=response_create_car_chassis.id,
        dimensions_id=response_create_car_dimensions.id,
        interior_id=response_create_car_interior.id
    )
    
    data = await CarEntityService.create(self=repo, car=car_data)
    return data


@router.delete("/car_entity/{id}")
async def delete(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CarEntityService(session)
    data = await CarEntityService.delete(self=repo, car_id=id)
    return data


@router.put("/car_entity/{car_id}")
async def update(car_id: int, car_dto: CarTotalDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = CarEntityService(session)
    repo_chassis = ChassisService(session)
    repo_engine = EngineService(session)
    repo_dimensions = DimensionsService(session)
    repo_interior = InteriorService(session)

    car = CarEntity(
        vin_id=car_dto.vin_id,
        country_manufacturer=car_dto.country_manufacturer,
        description=car_dto.description,
        brand=car_dto.brand,
        model=car_dto.model,
        year_of_release=car_dto.year_of_release,
        photos=car_dto.photos,
        mileage=car_dto.mileage,
        gear_box=car_dto.gear_box,
        drive=car_dto.drive,
        condition=car_dto.condition,
        body_type=car_dto.body_type,
        color=car_dto.color,
    )
    response_update_car_entity = await CarEntityService.update(self=repo, car_id=car_id, car_data=car)

    chassis_data = CarChassis(
        expenditure=car_dto.expenditure,
        overclocking=car_dto.overclocking,
        quantity_places=car_dto.quantity_places,
        volume_trunk=car_dto.volume_trunk
    )

    engine_data = CarEngine(
        turbine=car_dto.turbine,
        engine_type=car_dto.engine_type,
        engine_cylinders=car_dto.engine_cylinders,
        volume_engine=car_dto.volume_engine,
        power_hp=car_dto.power_hp,
        power_nm=car_dto.power_nm
    )

    dimensions_data = CarDimensions(
        clearance=car_dto.clearance,
        width=car_dto.width,
        height=car_dto.height,
        length=car_dto.length,
        wheelbase=car_dto.wheelbase,
        front_track=car_dto.front_track,
        rear_track=car_dto.rear_track
    )

    interior_data = CarInterior(
        conditioner=car_dto.conditioner,
        safety=car_dto.safety,
        steering_control_material=car_dto.steering_control_material,
        steering_control_side=car_dto.steering_control_side,
        steering_control_type_of_amplifier=car_dto.steering_control_type_of_amplifier,
        climate=car_dto.climate,
        wheel_diameter=car_dto.wheel_diameter,
        anti_theft=car_dto.anti_theft,
        help_driving=car_dto.help_driving,
        salon_material=car_dto.salon_material,
        salon_hatch=car_dto.salon_hatch,
        salon_color=car_dto.salon_color,
        heated=car_dto.heated,
        electric=car_dto.electric,
        head_lights_type=car_dto.head_lights_type,
        head_lights_washers=car_dto.head_lights_washers,
        multumedia=car_dto.multumedia,
        quantity_speaker=car_dto.quantity_speaker,
        subwoofer=car_dto.subwoofer,
        memory=car_dto.memory
    )



    response_update_car_chassis = await ChassisService.update(self=repo_chassis, chassis_id=response_update_car_entity["chassis_id"], chassis_data=chassis_data)
    response_update_car_engine = await EngineService.update(self=repo_engine, engine_id=response_update_car_entity["engine_id"], engine_data=engine_data)
    response_update_car_dimension = await DimensionsService.update(self=repo_dimensions, dimensions_id=response_update_car_entity["dimensions_id"], dimensions_data=dimensions_data)
    response_update_car_interior = await InteriorService.update(self=repo_interior, interior_id=response_update_car_entity["interior_id"], interior_data=interior_data)

    return response_update_car_entity, response_update_car_chassis, response_update_car_engine, response_update_car_dimension, response_update_car_interior


@router.put("/chassis/{id}")
async def update_chassis(id: int, chassis_dto: ChassisDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = ChassisService(session)

    chassis_data = CarChassis(
        expenditure=chassis_dto.expenditure,
        overclocking=chassis_dto.overclocking,
        quantity_places=chassis_dto.quantity_places,
        volume_trunk=chassis_dto.volume_trunk
    )

    data = await ChassisService.update(self=repo, chassis_id=id, chassis_data=chassis_data)
    return data

@router.put("/engine/{id}")
async def update_engine(id: int, engine_dto: EngineDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = EngineService(session)

    engine_data = CarEngine(
        turbine=engine_dto.turbine,
        engine_type=engine_dto.engine_type,
        engine_cylinders=engine_dto.engine_cylinders,
        volume_engine=engine_dto.volume_engine,
        power_hp=engine_dto.power_hp,
        power_nm=engine_dto.power_nm
    )

    data = await EngineService.update(self=repo, engine_id=id, engine_data=engine_data)
    return data

@router.put("/dimensions/{id}")
async def update_dimensions(id: int, dimensions_dto: DimensionsDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = DimensionsService(session)

    dimensions_data = CarDimensions(
        clearance=dimensions_dto.clearance,
        width=dimensions_dto.width,
        height=dimensions_dto.height,
        length=dimensions_dto.length,
        wheelbase=dimensions_dto.wheelbase,
        front_track=dimensions_dto.front_track,
        rear_track=dimensions_dto.rear_track
    )

    data = await DimensionsService.update(self=repo, dimensions_id=id, dimensions_data=dimensions_data)
    return data

@router.put("/interior/{id}")
async def update_interior(id: int, interior_dto: InteriorDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = InteriorService(session)

    interior_data = CarInterior(
        conditioner=interior_dto.conditioner,
        safety=interior_dto.safety,
        steering_control_material=interior_dto.steering_control_material,
        steering_control_side=interior_dto.steering_control_side,
        steering_control_type_of_amplifier=interior_dto.steering_control_type_of_amplifier,
        climate=interior_dto.climate,
        wheel_diameter=interior_dto.wheel_diameter,
        anti_theft=interior_dto.anti_theft,
        help_driving=interior_dto.help_driving,
        salon_material=interior_dto.salon_material,
        salon_hatch=interior_dto.salon_hatch,
        salon_color=interior_dto.salon_color,
        heated=interior_dto.heated,
        electric=interior_dto.electric,
        head_lights_type=interior_dto.head_lights_type,
        head_lights_washers=interior_dto.head_lights_washers,
        multumedia=interior_dto.multumedia,
        quantity_speaker=interior_dto.quantity_speaker,
        subwoofer=interior_dto.subwoofer,
        memory=interior_dto.memory
    )

    data = await InteriorService.update(self=repo, interior_id=id, interior_data=interior_data)
    return data
