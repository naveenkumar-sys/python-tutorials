amount = 15000
discount_percentage = 20
gst_percentage = 18

def billing():
    dis_amount = amount * discount_percentage/100
    gst_price = dis_amount * gst_percentage/100
    return amount + gst_price 

price =billing()
print(price)