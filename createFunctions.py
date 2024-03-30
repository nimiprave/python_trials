#creating functions

car = {
    "name" : "Subaru",
    "model" : "Forester",
    "kilometer" : 500,
    "gas" : 40
 }


def get_milege(car):
    return car["kilometer"] / car["gas"]


def get_name(car):
    return f"{car['name']}{car['model']}"


def print_car(car):
    print(f"{get_name(car)} has milege of {get_milege(car)}")

print(get_milege(car))

print_car(car)