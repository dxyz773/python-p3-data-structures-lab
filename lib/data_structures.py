spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    test = [key["name"] for key in spicy_foods]
    return test


def get_spiciest_foods(spicy_foods):
    test_1 = [key for key in spicy_foods if key["heat_level"] > 5]
    return test_1


def print_spicy_foods(spicy_foods):
    for key in spicy_foods:
        print(
            f'{key["name"]} ({key["cuisine"]}) | Heat Level: {key["heat_level"] * "🌶"}'
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for key in spicy_foods:
        if key["cuisine"] == cuisine:
            return key


def print_spiciest_foods(spicy_foods):
    for key in spicy_foods:
        if key["heat_level"] > 5:
            print(
                f'{key["name"]} ({key["cuisine"]}) | Heat Level: {key["heat_level"] * "🌶" }'
            )


def get_average_heat_level(spicy_foods):
    average = 0
    for key in spicy_foods:
        average += key["heat_level"]
    return int(average / len(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
