class RetailItem:
    def __init__(self, description, quantity, price):
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    def get_all(self):
        return self.__description, self.__quantity, self.__price

    def get_descriprion(self):
        return self.__description

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

