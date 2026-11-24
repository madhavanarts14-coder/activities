x = 5
if type(x) is int:
    print("true")
else:
    print("false")

x = 5.5
if type(x) is float:
    print("true")
else:
    print("false")

x = 7
y = 7
if x is y:
    print("x and y has same identity")

y = 11
if x is not y:
    print("x and y has different identity")

