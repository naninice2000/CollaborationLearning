from inventory import Inventory
import time
print " Create your Resturent inventory "
print " "
ID = int(raw_input("enter the order number:"))
pname = raw_input(" Enter Product Name: " )
#ING = raw_input(" Enter INGREDENT: ")
Quantity = int(raw_input(" Enter How many needed: "))
Price = raw_input(" Enter Price: ")
Price = float(Price)


#orderdate= raw_input(" Enter Date: ")


Product_obj = Inventory()
Product_obj.setProductID(ID)
Product_obj.setProductName(pname)
#Product_obj.setProductIngredent(ING)
Product_obj.setProductQuantity(Quantity)
Product_obj.setProductPrice(Price)


print "\n"
print "ID"
print Product_obj.getProduct_ID()
print "\n"
print "Product_Name: " 
print Product_obj.getProductName()
print "\n"
print  "Product_Ingredient: " 
print Product_obj.getProductIngredent()
print "\n"
print "Product_Quantity " 
print Product_obj.getProductQuantity()
print "\n"
print "product_price: $" 
print Product_obj.getProductPrice()
print "\n"
print "ProductTotalPrice : $" 
print Product_obj.getProductTotalPrice()
print "\n"
print "Product orderdate " 
print Product_obj.getProductorderdate()
print "\n"





