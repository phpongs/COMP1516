# jason wilder

def test():
    i = 1

    while i <= 1000:
        print(i)
        if i >= 5:
            return  # break
        i += 1

    print("bye")


test()
print("the end")

