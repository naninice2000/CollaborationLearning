import datetime

class Inventory:
	ID = ""
	Product_name = "" 
	Product_ingredent= ['salt','chilli']
	Product_quantity = ""
	Product_price = ""
	Total =""
	Product_orderdate= datetime.date.today()
	
	
		
	
	def __init__(self):
		print" Product Name and quantity"

	def setProductID(self, ID):
		self.Product_ID = ID
	
	
	def setProductName(self, pname):
		self.Product_name = pname
		
	def setProductIngredent(self, ING):
		self.Product_ingredent.append(ING)

	def setProductQuantity(self, Quantity):
		self.Product_Quantity = Quantity
	
	def setProductPrice(self, Price):
		self.Product_Price = Price 

	

	def setProductTotalPrice(self, Quantity, Price):
		self.Product_Quantity = Quantity
		self.Product_Price = Price

	def setProductorderdate(self, OrderDate):
		self.Product_orderdate = OrderDate


	

	
	def getProduct_ID(self):
		ID = self.Product_ID
		return ID

	def getProductName(self):
		pname = self.Product_name
		return pname

	def getProductIngredent(self):
		Product_ingredent = self.Product_ingredent
		return Product_ingredent
	
	def getProductQuantity(self):
		Product_Quantity = 	self.Product_Quantity
		return Product_Quantity
	
	def getProductPrice(self):
		Product_Price = self.Product_Price 
		return Product_Price

   
	def getProductTotalPrice(self):
		Total=self.Product_Quantity * self.Product_Price
		return Total

	
	def getProductorderdate (self):
		return self.Product_orderdate