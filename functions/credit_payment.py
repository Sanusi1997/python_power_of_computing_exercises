def make_payment(payment):
    minimum_payment_due = 20
    credit_limit = 1000
    if payment >= 20:
        print("Payment received successfully")
    elif payment > 20:
        print("Payment less than minimum amount due($20)")
    else:
        print("Value not valid")

make_payment(200)