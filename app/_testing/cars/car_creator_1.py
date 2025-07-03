import json
import random
from typing import List

def generate_random_cars(count: int) -> str:
    brands = ["Toyota", "BMW", "Mercedes", "Audi", "Ford", "Honda", "Volkswagen"]
    models = {
        "Toyota": ["Camry", "Corolla", "RAV4", "Land Cruiser"],
        "BMW": ["X5", "3 Series", "5 Series", "7 Series"],
        "Mercedes": ["C-Class", "E-Class", "S-Class", "GLE"],
        "Audi": ["A4", "A6", "Q5", "Q7"],
        "Ford": ["Focus", "Mustang", "Explorer", "F-150"],
        "Honda": ["Civic", "Accord", "CR-V", "Pilot"],
        "Volkswagen": ["Golf", "Passat", "Tiguan", "Touareg"]
    }
    colors = ["Black", "White", "Silver", "Gray", "Red", "Blue", "Green"]
    gear_boxes = ["Automatic", "Manual", "CVT", "DSG"]
    body_types = ["Sedan", "SUV", "Coupe", "Hatchback", "Pickup"]
    engine_types = ["Gasoline", "Diesel", "Hybrid", "Electric"]
    
    cars = []
    
    for i in range(count):
        brand = random.choice(brands)
        model = random.choice(models[brand])
        year = random.randint(2000, 2023)
        vin = ''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=17))
        
        car = {
            "vin_id": vin,
            "country_manufacturer": "Germany" if brand in ["BMW", "Mercedes", "Audi", "Volkswagen"] else random.choice(["Japan", "USA", "Korea"]),
            "description": f"Excellent condition {brand} {model}, {year} year",
            "brand": brand,
            "model": model,
            "year_of_release": year,
            "photos": [f"https://example.com/cars/{brand}_{model}_{year}_{i}.jpg"],
            "mileage": random.randint(1000, 200000),
            "gear_box": random.choice(gear_boxes),
            "drive": random.choice(["FWD", "RWD", "AWD"]),
            "condition": random.choice(["New", "Used", "Certified Pre-Owned"]),
            "body_type": random.choice(body_types),
            "color": random.choice(colors),
            "turbine": random.choice([True, False]),
            "engine_type": random.choice(engine_types),
            "engine_cylinders": random.choice([4, 6, 8]),
            "volume_engine": round(random.uniform(1.5, 5.0), 1),
            "power_hp": random.randint(100, 500),
            "power_nm": random.randint(150, 700),
            "expenditure": round(random.uniform(5.0, 15.0), 1),
            "overclocking": round(random.uniform(5.0, 15.0), 1),
            "quantity_places": random.choice([2, 4, 5, 7]),
            "volume_trunk": random.randint(300, 800),
            "clearance": random.randint(120, 250),
            "width": random.randint(1700, 2000),
            "height": random.randint(1400, 1800),
            "length": random.randint(4000, 5200),
            "wheelbase": random.randint(2500, 3100),
            "front_track": random.randint(1500, 1700),
            "rear_track": random.randint(1500, 1700),
            "conditioner": random.choice([True, False]),
            "safety": random.choice(["ABS, ESP, Airbags", "Full safety package"]),
            "steering_control_material": random.choice(["Leather", "Plastic", "Wood"]),
            "steering_control_side": random.choice(["Left", "Right"]),
            "steering_control_type_of_amplifier": random.choice(["Electric", "Hydraulic"]),
            "climate": random.choice(["Automatic", "Manual", "Dual-zone"]),
            "wheel_diameter": random.choice([16, 17, 18, 19, 20]),
            "anti_theft": random.choice(["Alarm", "Immobilizer", "GPS tracking"]),
            "help_driving": random.choice(["Parking sensors", "Camera", "360 view"]),
            "salon_material": random.choice(["Leather", "Alcantara", "Fabric"]),
            "salon_hatch": random.choice([True, False]),
            "salon_color": random.choice(colors),
            "heated": random.choice(["Front seats", "All seats", "Steering wheel"]),
            "electric": random.choice(["Windows", "Mirrors", "All"]),
            "head_lights_type": random.choice(["Halogen", "LED", "Xenon"]),
            "head_lights_washers": random.choice([True, False]),
            "multumedia": random.choice(["Basic", "Premium", "Navigation"]),
            "quantity_speaker": random.choice([4, 6, 8, 12]),
            "subwoofer": random.choice([True, False]),
            "memory": random.choice(["8GB", "16GB", "32GB"])
        }
        
        cars.append(car)
    
    return json.dumps(cars, ensure_ascii=False, indent=4)

# Генерация 5 случайных автомобилей и вывод JSON
random_cars_json = generate_random_cars(2)
print(random_cars_json)
