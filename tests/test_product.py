import pytest

from src.my_class import Product


def test_class_product(product_return_1):
    assert product_return_1.name == "Samsung Galaxy S23 Ultra"
    assert product_return_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_return_1.price == 180000.0
    assert product_return_1.quantity == 5


def test_new_product(new_product_classmethod):
    new_product = Product.new_product(new_product_classmethod)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price(capsys, new_product_classmethod):
    new_price = Product.new_product(new_product_classmethod)
    new_price.price = 100
    assert new_price.price == 100
    new_price.price = -120
    mess = capsys.readouterr()
    assert (
        mess.out.strip().split("\n")[-1]
        == "Цена не должна быть нулевая или отрицательная"
    )


def test_str(product_str):

    assert str(product_str[0]) == "Samsung, 180000.0 руб. Остаток: 5 шт."
    assert str(product_str[1]) == "Iphone, 210000.0 руб. Остаток: 8 шт."
    assert str(product_str[2]) == "Xiaomi, 31000.0 руб. Остаток: 14 шт."


def test__add__(product__add__):
    assert product__add__[0] == 2580000.0
    assert product__add__[1] == 1334000.0
    assert product__add__[2] == 2114000.0


def test_smartphone(smartphone_return):
    assert smartphone_return.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_return.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_return.price == 180000.0
    assert smartphone_return.quantity == 5
    assert smartphone_return.efficiency == 95.5
    assert smartphone_return.model == "S23 Ultra"
    assert smartphone_return.memory == 256
    assert smartphone_return.color == "Серый"


def test_lawngrass(lawngrass_return):
    assert lawngrass_return.name == "Газонная трава"
    assert lawngrass_return.description == "Элитная трава для газона"
    assert lawngrass_return.price == 500.0
    assert lawngrass_return.quantity == 20
    assert lawngrass_return.country == "Россия"
    assert lawngrass_return.germination_period == "7 дней"
    assert lawngrass_return.color == "Зеленый"


def test_sum_smartphone(sum_test_phone):
    res = sum_test_phone[0] + sum_test_phone[1]
    assert res == 2580000.0


def test_sum_grass(sum_test_grass):
    res = sum_test_grass[0] + sum_test_grass[1]
    assert res == 16750.0


def test_sum_error_grass_and_phone(sum_test_grass, sum_test_phone):
    with pytest.raises(TypeError):
        res = sum_test_grass[0] + sum_test_phone[0]


def test_sum_error_phone_and_num(sum_test_phone):
    with pytest.raises(TypeError):
        res1 = sum_test_phone[0] + 1


def test_sum_error_grass_and_num(sum_test_grass):
    with pytest.raises(TypeError):
        res1 = sum_test_grass[0] + 1


def test_value_error_product():
    with pytest.raises(ValueError) as e:
        res1 = Product("Samsung", "256GB", 180000.0, 0)

    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"
