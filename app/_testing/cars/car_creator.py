# _testing/cars/car_creator.py
import random
from typing import Dict, Any

def generate_car_chassis() -> Dict[str, Any]:
    return {
        "gear_box": random.choice(["Automatic", "Manual", "CVT", "DSG"]),
        "drive": random.choice(["FWD", "RWD", "AWD"]),
        "brake_system": random.choice(["ABS", "ESP", "Regenerative"]),
        "suspension_type": random.choice(["Multilink", "MacPherson", "Solid Axle"]),
    }

def generate_car_engine() -> Dict[str, Any]:
    return {
        "engine_type": random.choice(["Gasoline", "Diesel", "Hybrid", "Electric"]),
        "engine_cylinders": random.choice([4, 6, 8]),
        "volume_engine": round(random.uniform(1.5, 5.0), 1),
        "power_hp": random.randint(100, 500),
        "power_nm": random.randint(150, 700),
    }

def generate_car_dimensions() -> Dict[str, Any]:
    return {
        "length": random.randint(4000, 5200),
        "width": random.randint(1700, 2000),
        "height": random.randint(1400, 1800),
        "wheelbase": random.randint(2500, 3100),
        "clearance": random.randint(120, 250),
    }

def generate_car_interior() -> Dict[str, Any]:
    return {
        "salon_material": random.choice(["Leather", "Alcantara", "Fabric"]),
        "salon_color": random.choice(["Black", "Beige", "Gray"]),
        "heated_seats": random.choice([True, False]),
        "ventilated_seats": random.choice([True, False]),
    }

def generate_full_car_data() -> Dict[str, Any]:
    return {
        "vin_id": ''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=17)),
        "brand": random.choice(["Toyota", "BMW", "Mercedes"]),
        "model": random.choice(["Camry", "X5", "C-Class"]),
        "year_of_release": random.randint(2000, 2023),
        "chassis": generate_car_chassis(),
        "engine": generate_car_engine(),
        "dimensions": generate_car_dimensions(),
        "interior": generate_car_interior(),
    }