""" . Design a class called Bill that has fields to store the list of items, their prices per unit,
quantity of each item in the bill, and the grand total of the items. Create an overloaded
add operator so that when you add two bills, you get a new bill with all the items in
the two bills (there may be duplicates in the final bill) and a new grand total.
Would you have multiply and divide overloaded operators in this case? Think!
For example, a McDonald’s bill might include 2 burgers @ $4.00 each, 4 strawberry
milkshakes @ $2.50 each
"""

class Bill(object):
    def __init__(self, items_list, product = " ", unit_price = 0.0, item_quantity = 0, grand_total = 0.0 ):
        self.items = items_list
        self.product_name = product
        self.unit_price_int = unit_price
        self.item_qty_int = item_quantity
        self.total_int = grand_total
    def calc_total(self):
        self.total_int = self.item_qty_int * self.unit_price_int
        return self.total_int

    def buy_item(self, item):
        item.append(self.unit_price_int)
        item.append(self.item_qty_int)
        item.append(Bill.calc_total(self))
        self.items.append(item)

    def __str__(self):
        return "Price of {}: ${}| Quantity of {} purchased: {}| Total purchase: ${}".format(self.product_name,
            self.items[0][0],self.product_name, self.items[0][1], self.items[0][2])

cus_list = list()
total_list = list()
customer = Bill(total_list,"Indomie", 25.0, 2,0)
customer.calc_total()
customer.buy_item(cus_list)
print(customer)