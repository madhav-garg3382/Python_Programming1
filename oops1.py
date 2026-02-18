def mileage(engine, weight, tyre):
    result = 28 - (4 * engine) - (0.006 * (weight - 1000)) - (0.7 * (tyre - 15)) 
    # 28 - 4 * engine_l - 0.006 * (weight_kg - 1000) - 0.7 * (tyre_in - 15)
    
    if result < 5:
        result = 5
    return result


def city_highway(engine, weight, tyre):
    base = mileage(engine, weight, tyre)
    city = base * 0.85
    highway = base * 1.10
    return base, city, highway



engine = 1.5
weight = 1200
tyre = 16

base, city, highway = city_highway(engine, weight, tyre)

print("Engine:", engine, "L")
print("Weight:", weight, "kg")
print("Tyre:", tyre, "inch")
print("Base mileage:", base, "km/L")
print("City mileage:", city, "km/L")
print("Highway mileage:", highway, "km/L")
