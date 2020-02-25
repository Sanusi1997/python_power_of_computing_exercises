"""You buy an international calling card to India. The calling card company has some
special offers.
(a) If you charge your card with $5 or $10, you don’t get anything extra.
(b) For a $25 charge, you get $3 of extra phone time.
(c) For a $50 charge, you get $8 of extra phone time.
(d) For a $100 charge, you get $20 of extra phone time."""
def recharge_offers():
    recharge_offers = {
                        1:"Recharge $5 or $10 for no bonus",
                        2:"Recharge $25 and get $3 extra phone time",
                        3:"Recharge $50 and get $8 extra phone time",
                        4: "Recharge $100 and get $20 extra phone time"
                       }
    return recharge_offers

def buy_card():
    for key, elements in recharge_offers().items():
        print (key,elements)

    recharge_amount = int(input("Please enter your choice of recharge from the display above:  "))
    if recharge_amount == 5 or recharge_amount==10:
        return print(f"You have recharged your line with ${recharge_amount}")
    elif recharge_amount == 25:
        new_amount = recharge_amount + 3
        return print(f"You have recharged your line with ${new_amount}")
    elif recharge_amount == 50:
        new_amount = recharge_amount + 8
        return print(f"You have recharged your line with ${new_amount}")
    elif recharge_amount == 100:
        new_amount = recharge_amount + 20
        return print(f"You have recharged your line with ${new_amount}")
    else:
        print("Thanks for checking out our offers, run the program again to see offers again!")
buy_card()