def test_class_category(category_return_1):
    assert category_return_1.name == "Смартфоны"
    assert (
        category_return_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_return_1.category_count == 1
    assert category_return_1.product_count == 3
