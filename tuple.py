a=(1,2,3,4,5)
print(a)

# check
print(type(a))
# a.append("4")  ((ADD ELEMENT USING APEND...BUT THE ELEMENT DISPLY IN LAST))
print(a)

# tuple adding

a=(1,2,3,)
b=list(a)
b.append(4)
print(b)
a=tuple(b)
print(a)


a=(1,2,3,4)
b=list(a)
a.append(20)
print(b)
a=tuple(b)
print(a)


# clear
z={1,2}
z.clear()
print(z)