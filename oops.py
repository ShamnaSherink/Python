# class Car:
#       def __init__(self,price,color,name):
#             self.price=price
#             self.color=color
#             self.name=name
#       def   start(self):
#             print(f'{self.name}-engin started') 
# car1=Car(price=100000,color="black",name="bmw")
# car2=Car(price=100000,color="white",name="audi") 
# print(car1.name,car1.price,car1.color)            
# car1.start()  


# class Phones:
#       def __init__(self,price,color,brand):
#             self.price=price
#             self.color=color
#             self.brand=brand
#       def start(self):
#           print(f'{self.brand}-mobile working')
# mobile1=Phones(price=200000,color="white",brand="apple")
# mobile2=Phones(price=20000,color="black",brand="samsung")
# print(mobile1.price,mobile1.color,mobile1.brand)
# mobile1.start()





#INHERITENCE:-

# class Person:
#      def __init__(self,name,contact):
#           self.name=name
#           self.contact=contact
#      def  adress(self): 
#          print(self.name,self.contact)    
# class Doctor(Person):
#  pass
# class Patient(Person):
#  pass

# Doctor1=Person("shamna",9072169745)
# Patient2=Person("rasha",9876543589)
# Doctor1.adress()
# Patient2.adress()            





# CALCULATE THE AREA AND PERIMETRE OF A CIRCLE:-

# import math  
# class Circle:
#       def __init__(self,radius):
#             self.radius=radius 

#       def area(self):
#           return math.pi*self.radius
#       def perimeter(self):
#           return 2*math.pi*self.radius
# a=float(input("enter a radius "))
# result= Circle(a)
# print(result.area())
# # b=float(input("entera a perimetre"))
# # result=Circle(b)
# print(result.perimeter())





# MAKE A CALCULATOR:-



# class Calculator:
#      def add(self,x,y):
#           return x+y
#      def sub(self,x,y):
#           return x-y
#      def multiply(self,x,y):
#           return x*y
#      def divide(self,x,y):
#           return x/y
# x=int(input("enter the first number:"))
# y=int(input("enter the second number:"))  
# result=Calculator()
# print(result.add(x,y)) 
# print(result.sub(x,y))
# print(result.multiply(x,y)) 
# print(result.divide(x,y))







# FIND THE PERSON AGE USING THEIR DATE OF BIRTH:- OUTPUT=(AGE OF SHERIN IS 21)


# from datetime import date,datetime
# class Person:
#       def __init__(self,name,country,dob):
#            self.name=name
#            self.country=country
#            self.dob=dob
#       def get_age(self):
#            today=datetime.today()
#            dob_date=datetime.strptime(self.dob,"%Y-%m-%d")
#            age=today.year-dob_date.year
#            return  age
                
# name=input("enter a name")
# country=input("enter the country")
# dob=(input("enter the dob(YYYY-MM-DD)"))
# person=Person(name,country,dob)
# print("Age of",person.name,"is",person.get_age())






#FIND THE SUM AND REVERSE THE DIGIT OR STRING:-

# class Mycalculations:
#      def digits(number):
#           digit_sum=sum(int(digits) for digits in str(number) )       
#           return digit_sum
#      def reverse(value):
#           if isinstance(value,int):
#               return int(str(value)[::-1] )
#           elif isinstance(value,str):
#                return value[::-1]
#           else:
#                return "invalid output,please provide a number or a string"
# a=(input("enter a number"))     
# result= Mycalculations()
# s=result.digits(a)
# print(s)





class Mycalculations:
    @staticmethod
    def digits(number):
        digit_sum = sum(int(digit) for digit in str(number))
        return digit_sum
    
    @staticmethod
    def reverse(value):
        if isinstance(value, int):
            return int(str(value)[::-1])
        elif isinstance(value, str):
            return value[::-1]
        else:
            return "Invalid output, please provide a number or a string"

a = input("Enter a number: ")
result = Mycalculations()

s = result.digits(a)
print("Sum of digits:", s) 

z=input("enter a string")
result=Mycalculations()

y=result.reverse(z)
print("reverse of a number",y)








          



class Shape:
     def display(self):
         print("this is shape")

class Rectangle (Shape):
      def display(self):
           print("this is rectangular")
class  Circle(Shape) :
      def display(self):
           print("this is circular shape")
                 
class   Square(Rectangle):
         def display(self):
              print("square is rectangle")
rectangle=Rectangle()
circle=Circle()
square=Square()

 

rectangle.display()
circle.display()
square.display()
 

