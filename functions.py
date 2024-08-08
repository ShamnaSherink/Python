# build in functionn

# def message ():
#     print("hai")
# message("sherin")    


# print 2 names:-

# def message(name):
#     print("hai "+name)
# message("sherin") 
   

# add two nmbrs:-

# def message (num1,num2):
#     print(num1+num2)
# message(2,4)   
#  

# multiple 3 numbers:-

# def message (num1,num2,num3):
#     print(num1*num2*num3)
# message(1,2,3) 

   
# square of number:-

# def message (num):
#     print(num*num)
# message(10) 


# find largest number:-

# def message(num1,num2,num3):
#       if (num1>=num2) and (num1>=num3):
#            print("num1 is largest number")
#       elif (num2>=num1)and(num2>=num3):
#             print("num2 is largest number")
#       else:
#           print("num3  is largest")
# message(3,6,9)    


#  find sum of the numbers:-

# def sum (numbers):
#     total=0
#     for i in numbers:
#        total=total+i
#     return total
    # print(sum((9,2,1,7,5)))



# multiple of the numbers:-

# def message (numbers):
#     total=1
#     for i in numbers:
#         total=total*i
#     return total
# print(message((9,2,1,7,5)))

  
# def message(numers):
#     total=1
#     for i in range(1,10,2):
#         total=total*i
#     return total
# message()  



# def multiplication(number,limit):
#   for i in range(1,limit+1):
#      result=(number*i)
#      print(result)
# a=int(input("enter a number"))
# b=int(input("enter a limit"))
# print(multiplication(a,b))



# num=(int(input("enter limit")))
# a=0
# b=1
# print(a)
# print(b)

# for i in range(num):
#    c=a+b
#    print(c)
#    a=b
#    b=c

# using fibanocci:-.

# def fibanocci (limit):
#    a=0
#    b=1
#    print(a)
#    print(b)
#    for i in range(limit+1):
#       c=a+b
#       print(c)
#       a=b
#       b=c
# a=int(input("enter a limit"))     
# print(fibanocci(a))


# factoria


# def factorial (limit):
#     fact=1
#     for i in range(1, limit+1):
#       fact=fact*i
#     print(fact)
# a=int(input("enter the limit"))
# print(factorial(a))
   



#  palindrome eg( mom, malayalam)

# a=input("enter a string")
# a=(a.lower())
# b=a[::-1]

# if a==b:
#    print("palandrome")
# else:
#    print("not palandrome")   

   

# palindrome:-

# def palindrome(z):
# z=z.lower()
#    return z==z[::-1]
# a=(input("enter a string"))
# if palindrome(a):
#    print("palindrome")
# else:
#    print("not palindrome")  




# def palindrome(z):
#      z=str(z)
#      return z==z[::-1]
# a=int(input("enter a number"))
# if palindrome(a):
#    print("palindrome")
# else:
#    print("not palindrome")



   # power
# def power(base,exponent):
#        a=1
#        for i in range(exponent):
#            a=a*base
#        return(a)
# b=int(input("enter base"))
# c=int(input("enter exponent"))
# result=power(b,c)
# print(result)





# newwww:-

# def message():
#      print("hai")
# message()

# def message(name):
#      print("hai "+name)
# message("sherin")     
   
# def sum(a,b):
#      print(a+b)
# sum(2,3)  

# def message(a,b,c):
#      print(a*b*c)
# message(1,2,3)     

   
   
# def message(a):
#      print(a*a)
# message(5)  


# def message(a,b,c):
#     if (a >b) and(a>c):
#      return a
    
#     elif (b>a)  and(b>c)   :
#        return b
#     else:
#       return c
# a=message(4,6,8)   
# print(a)


#    largest nmbr:-  
# def message(a,b,c):
#     if (a >b) and(a>c):
#      print(a)
   
#     elif (b>a)  and(b>c)   :
#      print(b)
#     else:
#      print(c)
# a=message(4,6,8) 
# print(a,"is largest")


# def sum (number):
#  a=0
#  for i in number:
#    a=a+i
#  return(a)  
# a=sum((1,2,3,4,5)) 
# print(a)


#      result=(number*i)
#      print(result)
# a=int(input("enter a number"))
# b=int(input("enter a limit"))
# print(multiplication(a,b))




# def multiplication(number,limit):
#   for i in range(1,limit+1):
#          result=(number*i)
#          print(result)
# a=int(input("enter a number"))
# b=int(input("enter a limit"))
# print(multiplication(a,b))



# prime number:=


# def primes(a):
#    if a<=1:
#       return False
#    if a<=3:
#       return  True
#    for  i in range(2,int(a**0.5)+1):
#     if a%i==0:
#       return False
#    return True
# b=int(input("enter a number"))
# print(b)
# if primes(b):
#   print("prime number")
# else:
#   print("not a prime number")  
  
  
  
#   factorial

# def message():
#     b=int(input("enter a number"))
#     total=1
#     if b<0:
#        print("not factorial is one")
#     elif (b==0) or(b==1):
#        print("factorial number")
#     else:
#        for i in range(2,b+1):
#         total=total*i
#        print(total)
# message()       
       
       
  
     
# recursia:
# def fact(n):
#  if n==0 or n==1:
#     return n
#  else:
#   return n*fact(n-1)
# print (fact(5))  
 
       
          # power
# def power(base,exponent):
#        a=1
#        for i in range(exponent):
#            a=a*base
#        return(a)
# b=int(input("enter base"))
# c=int(input("enter exponent"))
# result=power(b,c)
# print(result)



# def power(base,exponent):
#    a=1
#    for i in range(1,exponent):
#       a=a*base
#    return(a)
# b=int(input("enter base"))
# c=int(input("enter exponent"))
# result=power(b,c)
# print(result)
#   return n*fact(n-1)



# power using reccursia:-

# def power(base,exponent):
#     a=1
#     for i in range(1,exponent):
#      return power(a=a*base)
# b=int(input("enter base"))
# c=int(input("enter exponent"))
# result=power(b,c)
# print(result)
        


# def power(base,exponent):
#    if exponent==0:
#        return 1
#    else:
#         return base*power(base,exponent-1)        
        
# b=int(input("enter a base"))
# c=int(input("enter exponent"))
# result=power(b,c)
# print(result)




# password generator:-
# import random
# def passwordgenerator(length):
#      a="abcd123hello324h765oljgsd345#/#lk?%&*"
#      b=""
#      for i in range(length):
#         b=b+random.choice(a)
#      return b
# z=int(input("enter length")   )
# result=passwordgenerator(z)
# print(result)  


# sum=lambda a,b: a+b 
# print(sum(2,4))


# list:-
# a=[1,2,3,4]
# b=list(map(lambda x :x*2,a))
# print(b)
   

# check even numbers:-

# a=[1,2,3,4,5,6,7,8,9,10]
# b=len(list(filter(lambda x:x%2==0,a)))                     
# print(b)
# c=len(list(filter(lambda x:x%2!=0,a)))
# print(c)



# user number:-

# a=[2,3,4,5,6,7]
# c=int(input("enter a number"))
# b=list(map(lambda x:x*c,a))
# print(b)



# count the numbers how many numbers used:-

# a=[1,2,3,4,5,6,1,2,3,4]
# b=int(input("enter count number"))
# c=dict(map(lambda x:(x,a.count(x)),set(a)))
# print(c)





fibonacci=lambda n:[0,1]if n==2 else fibonacci(n-1)+[fibonacci(n-1)[-1]+fibonacci(n-1)[-2]]
n=int(input("enter a number fibonacci number to generate"))
print ("Fibonacci series up to",n ," :",fibonacci(n))