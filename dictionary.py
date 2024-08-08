a={"name":"athira","age":"18","place":"clt"}
print(a)


# select one

b=a["name"]
print(b)


# add
a["name"]="haritha"
print(a)


a["email"]="haritha@gmail.com "
print(a)


# copyy

b=a.copy()
print(b)


# delete
a.pop("email")
print(a)


# all delete//

a.clear()
print(a)