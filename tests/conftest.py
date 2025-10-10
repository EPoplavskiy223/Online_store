import pytest

from src.my_class import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product_return_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def new_product_classmethod():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def category_return_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=["product1", "product2", "product3"],
    )


@pytest.fixture
def category_product_property():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return category1


@pytest.fixture
def product_str():
    product1 = Product("Samsung", "256GB", 180000.0, 5)
    product2 = Product("Iphone", "512GB", 210000.0, 8)
    product3 = Product("Xiaomi", "1024GB", 31000.0, 14)

    return product1, product2, product3


@pytest.fixture
def product__add__():
    product1 = Product("TEST1", "256GB", 180000.0, 5)
    product2 = Product("TEST2", "512GB", 210000.0, 8)
    product3 = Product("TEST3", "1024GB", 31000.0, 14)
    return product1 + product2, product1 + product3, product2 + product3


@pytest.fixture
def category_all_quantity():

    product1 = Product("test1", "qq", 180000.0, 5)
    product2 = Product("test2", "qq", 210000.0, 8)
    product3 = Product("test3", "qqq", 31000.0, 14)
    category1 = Category("TEST", "TEST!", [product1, product2, product3])
    return str(category1)


@pytest.fixture
def category_all_quantity_error():
    product1 = Product("test1", "qq", 180000.0, 5)
    product2 = Product("test2", "qq", 210000.0, -2)
    product3 = Product("test3", "qqq", 31000.0, 14)
    category1 = Category("TEST", "TEST!", [product1, product2, product3])
    return str(category1)


@pytest.fixture
def category__str__():
    product1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product2 = Product("TEST3", "1024GB", 31000.0, 14)

    category1 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product1, product2],
    )
    return str(category1)


@pytest.fixture
def smartphone_return():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def lawngrass_return():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def sum_test_phone():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    return smartphone1, smartphone2


@pytest.fixture
def sum_test_grass():
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    return grass1, grass2
