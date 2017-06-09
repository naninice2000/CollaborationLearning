class B:
  myfirstname = ""
  mylastname = ""
  myadress = ""
  myage = ""

  def __init__(self):
    print "Hi"
  def setFirstname(self,firstname):
    self.myfirstname = firstname
  def getFirstname(self):
    return self.myfirstname
  def setLastname(self,lastname):
    self.mylastname = lastname
  def getLastname(self):
    return self.mylastname
  def setAge(self,age):
    self.myage = age
  def getAge(self):
    return self.myage
  def setAdress(self,adress):
    self.myadress =adress
  def getAdress(self):
    return self.myadress