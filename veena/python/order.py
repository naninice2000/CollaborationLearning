from orderMng import order

print "\nOrder Management"
orderNumber=int(raw_input("\nEnter Order Number:"))
Date=raw_input("Enter The Date:")
CustomerDetails=raw_input("Enter the Customer Name:")
Items=raw_input("Enter the Items:")
TotalItems=int(raw_input("Enter total no of items:"))
Amount= raw_input("Enter the Amount:")
PaymentStatus=raw_input("Enter the PaymentStatus:")
OrderStatus=raw_input("Enter the OrderStatus:")
print "\n"

obj1=order()
obj1.setOrderNumber(orderNumber)
obj1.setOrderDate(Date)
obj1.setCustomerDetails(CustomerDetails)
obj1.setItemsOrdered(Items)
obj1.setTotalItems(TotalItems)
obj1.setTotalAmount(Amount)
obj1.setPaymentStatus(PaymentStatus)
obj1.setOrderStatus(OrderStatus)


print "\n"
print "Order Number         : ", obj1.getOrderNumber()
print "Date                 : ", obj1.getOrderDate()
print "Customer Details     : ", obj1.getCustomerDetails()
print "Items                : ", obj1.getItemsOrdered()
print "Total Number of Items: ", obj1.getTotalItems()
print "Amount               : ", obj1.getTotalAmount()
print "Payment Status       : ", obj1.getPaymentStatus()
print "OrderStatus          : ", obj1.getOrderStatus()
