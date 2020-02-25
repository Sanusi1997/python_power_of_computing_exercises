def purchase_item():
    cost_of_item = float(input("Please type the price of item purchased: "))
    membership = input("Kindly type True if you are a member or False if you are not: ")
    message = "Thanks for shopping with us and have a nice day!"
    if membership.title() == "True":
        discounted_price = cost_of_item - (cost_of_item * 0.15)
        return print("The price of the goods purchased is {:.2f} Naira"
            "\n{}".format(discounted_price, message))
    elif membership.title() == "False":
        discounted_price = cost_of_item - (cost_of_item * 0.05)
        return print("The price of the goods purchased is {:.2f} Naira"
                "\n{}".format(discounted_price, message))


purchase_item()
