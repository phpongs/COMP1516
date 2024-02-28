# jason wilder

x = 5


def do_something():
    global x  # on purpose, I want to change x from line 3
    x = 10000
    print(x)


print(x)
do_something()
print(x)
