class order:
	order_num=""
	order_date=""
	order_customerdetails=""
	order_itemsordered=""
	order_tolalitems=""
	order_totalamt=""
	order_paymentstatus=""
	order_status=""

	def __init__(self):
		print "Order Receipt"

	def setOrderNumber(self,OrderNumber):
		self.order_num=OrderNumber
	def setOrderDate(self,OrderDate):
		self.order_date=OrderDate
	def setCustomerDetails(self,CustomerDetails):
		self.order_customerdetails=CustomerDetails
	def setItemsOrdered(self,ItemsOrdered):
		self.order_itemsordered=ItemsOrdered
	def setTotalItems(self,TotalItems ):
		self.order_tolalitems=TotalItems
	def setTotalAmount(self,TotalAmount):
		self.order_totalamt=TotalAmount
	def setPaymentStatus(self,PaymentStatus):
		self.order_paymentstatus=PaymentStatus
	def setOrderStatus(self,Status):
	    self.order_status=Status

	def getOrderNumber(self):
		Number=self.order_num
		return Number
	def getOrderDate(self):
		Date=self.order_date
		return Date
	def getCustomerDetails(self):
		CustomerDetails=self.order_customerdetails
		return CustomerDetails
	def getItemsOrdered(self):
		Items=self.order_itemsordered
		return Items
	def getTotalItems(self):
		TotalItems=self.order_tolalitems
		return TotalItems
	def getTotalAmount(self):
		TotalAmount=self.order_totalamt
		return TotalAmount
	def getPaymentStatus(self):
		PaymentStatus=self.order_paymentstatus
		return PaymentStatus
	def getOrderStatus(self):
		Status=self.order_status
		return Status
	
	
	
	
	
	
	
	