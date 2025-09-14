# x = 5
# y = "parvez"
# print(x + y)


x = "programming language"


def myfunc():
    x = "fantastic"
    print("python is a " + x)


myfunc()

print("python is a " + x)


# global keyword
def myGlobalKeyord():
    global parvez
    parvez = "boy"
    print("he is a " + parvez)


myGlobalKeyord()

print("Parvez is a " + parvez)


y = "awesome"


def changeFunc():
    global y
    y = "ugly"


changeFunc()
print("javascript is a " + y + " language")
