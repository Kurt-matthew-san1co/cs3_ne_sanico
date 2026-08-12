def calculate_checkout(cart_total, shipping_speed):
    shipping_fee = ""
    if shipping_speed == "express":
        shipping_fee = 20
    elif shipping_speed == "overnight":
        shipping_fee = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping_fee = 0
    elif shipping_speed == "standard" and cart_total < 100:
        shipping_fee = 10
    else:
        shipping_fee = 0
        raise ValueError ("Invalid shipping type. Try again")

    final_bill = cart_total + shipping_fee
    return final_bill

print(calculate_checkout(110,"standard"))

