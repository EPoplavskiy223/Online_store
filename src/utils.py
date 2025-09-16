import json

from src.my_class import Category, Product


def read_json(data_user: str) -> list:
    """Читает файл формата json"""

    with open(data_user, "r", encoding="utf-8") as file:
        return json.load(file)


def distribution(data: list) -> list:
    """Распаковывает лист и передает словари в Классы"""
    result = []

    for category in data:
        result.append(Category(**category))
        for product in category["products"]:
            result.append(Product(**product))
    return result