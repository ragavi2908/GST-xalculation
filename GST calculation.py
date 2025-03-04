#GST Amount = (Selling Price x GST Rate) / 100.
# if a product or service costs Rs. 100 and the GST levied on that is 18%, 
# the GST amount will be 100 x 18% = Rs. 18.
#  The net amount you'd have to pay would be Rs. 118.
print("welcome Shoppsy")
gender_select=input("what gender you are:")
gender="1.female","2.male"
print("2.male" in gender)
print("jeans")
print("casuals")
print("crops")
print("formals")
jeans=900
casuals=450
crops=300
formals=650
your_need=input("what you prefer:")
quantity=3
print("jeans*quantity")
your_pick=int(input("No.of.collections:"))
mrb_price=jeans*3
gst_percentage=12
gst_price=your_pick*12/100
net_price=your_pick+gst_price+quantity+mrb_price
print(f"GST applied as {gst_price} for {gst_percentage}")
print(f"total purchased after applied gst is {net_price}")




















