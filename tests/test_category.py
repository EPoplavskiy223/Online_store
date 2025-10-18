def test_class_category(category_return_1):
    assert category_return_1.name == "Смартфоны"
    assert (
        category_return_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_return_1.category_count == 1
    assert category_return_1.product_count == 3


def test_category_product(category_product_property):

    assert category_product_property.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_valid_product(category_return_1, product_return_1):

    category_return_1._Category__products = []
    category_return_1.add_product(product_return_1)

    assert len(category_return_1._Category__products) == 1
    assert category_return_1._Category__products[0].name == "Samsung Galaxy S23 Ultra"


def test_all_quantity(category_all_quantity):

    assert category_all_quantity == "TEST, количество продуктов: 27 шт."


def test_all_quantity_error(capsys, category_all_quantity_error):
    mess = capsys.readouterr()

    assert mess.out.strip().split("\n")[-1] == "Отрицательное число товаров в test2"
    assert category_all_quantity_error == "TEST, количество продуктов: 19 шт."


def test_category__str__(category__str__):
    assert category__str__ == "Телевизоры, количество продуктов: 21 шт."


def test_middle_price(category_product_property):
    assert category_product_property.middle_price() == 140333.33


def test_no_quantity_middle(no_category_product):
    assert no_category_product.middle_price() == 0
