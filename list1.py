# list creation

a=["apple","mango","banana"]
print(a)


# length find

a=[1,2,3,4]
print(len(a))

b=["mango","apple","grapes"]
print(len(b))


# index Value

a=[1,2,3,4,5,6]
print(a[3])

a=[1,2,3,4,5,6,7,8,9,10]
print(a[8])
print(a[-1])
print(a[-2])

# combine

a=[1,2,3,4,5,6]
b=[7,8,9,10,11]
print(a+b)


# update

a=["potato","onion","carrot"]
a[2]="cabbage"
print(a)


a=[8,9,10,11,12,13]
a[3]=100
print(a) 
a.append(50)
print(a)
a.append(100)
print(a)
a.append("hello")
print(a)
# a.append(4,5,6)

# insert

a=[1,2,3]
a.insert(2,5)
print(a)

# extend

b=[4,5,6]
a.extend(b)
print(a)


# remove
a=[1,2,3,4]
a.remove(2)
print(a)
# a.remove(2,3)
# print(a)       cant add multiple element


# slicing

a=[1,2,3,4,5,6,7]
b=a[2:5]
print(b)




a=[10,11,12,13,14,15,16,17,18]
b=a[5:8]
print(b)

b=a[2:]
print(b)


b=a[:5]
print(b)

b=a[:]
print(b)

# print  2 nmbrs

a=[1,2,3,4,5]
b=a[1:2]+a[3:4]
print(b)

# clear list

a.clear()
print(a)

# clear all

del a
print(a)


c[1,2,3,4,5]
b=c
print(b)