class Product:
    """
    Атрибуты класса заполняются автоматически при инициализации нового объекта.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_amount):
        if new_amount >= 0:
            self.__price = new_amount
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """
    Атрибуты класса заполняются автоматически при инициализации нового объекта.
    """

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        products_str = ""
        for prod in self.__products:
            products_str += (
                f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
            )
        return products_str

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1
