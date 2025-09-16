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
