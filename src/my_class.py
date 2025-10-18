from src.Base_Product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
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
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError


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
        Category.product_count += len(self.__products)

    @property
    def products(self):
        products_str = ""
        for prod in self.__products:
            products_str += (
                f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
            )
        return products_str

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def all_quantity(self):
        """Подсчет общего количества товаров"""
        result = 0
        for prod in self.__products:
            if prod.quantity > 0:
                result += prod.quantity
            else:
                print(f"Отрицательное число товаров в {prod.name}")
        return result

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.all_quantity} шт."

    def middle_price(self):
        try:
            return round(
                sum([products.price for products in self.__products])
                / len(self.__products),
                2,
            )
        except ZeroDivisionError:
            return 0


class Smartphone(Product):

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
