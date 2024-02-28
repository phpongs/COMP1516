# jason wilder
x = 5

def c():
    global x
    print("c here")
    x = 10000
    print(x)

def b():
    print("hi from b")
    c()
    print("bye from b")
    print("whatever")
    print("the end")

def a(something):
    x = 20
    print(something.upper())
    b()

def main():
    a("jason")
    print("end of program")

if __name__ == '__main__':
    main()
