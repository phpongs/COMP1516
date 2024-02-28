# author: Pong, Alex

i = 410

while i <= 1100:
    if i % 100 != 0:    # is not a multiple of 100
        print(i, end=", ")
    i += 10

print('\nend\n')

i = 600

while i >= 412:
    print(i, end=', ')
    i -= 2

print('\nend\n')


i = 1
total = 0

while i <= 100:
    total += i
    i += 1

print('total is ' + str(total))
