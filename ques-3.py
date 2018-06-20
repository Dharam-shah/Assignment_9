class Temprature():

   def cf(self):
     far= int(input("Enter fahrenheit:"))
     x=((far-32)*(5/9))
     print("celsius is:",x)

   def Fc(self):
     celsius = int(input("Enter celsius:"))
     y = ((celsius*9/5)+32)
     print("Fahrenheit is:", y)

q = Temprature()
q.cf()
q.Fc

