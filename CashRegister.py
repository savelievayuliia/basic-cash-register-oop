from ua.univer.lesson.lesson06.retail_item.RetailItem_class import RetailItem

class CashRegister:
    def __init__(self, list_of_goods):
        self.list_of_goods = []

    def purchase_item(self, RetailItem):
        self.list_of_goods.append(RetailItem)

    def get_total(self):
        summ = 0
        for item in self.list_of_goods:
            summ += int(item.get_quantity()) * int(item.get_price())
        print("Total to checkout", summ, "USD")

    def show_items(self):
        for item in self.list_of_goods:
            print("Your cart consists of the following items: ", item.get_all())

    def clear(self):
        self.list_of_goods.clear()