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
    assert mess.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_str(product_str):

    assert str(product_str[0]) == "Samsung, 180000.0 руб. Остаток: 5 шт."
    assert str(product_str[1]) == "Iphone, 210000.0 руб. Остаток: 8 шт."
    assert str(product_str[2]) == "Xiaomi, 31000.0 руб. Остаток: 14 шт."


def test__add__(product__add__):
    assert product__add__[0] == 2580000.0
    assert product__add__[1] == 1334000.0
    assert product__add__[2] == 2114000.0
