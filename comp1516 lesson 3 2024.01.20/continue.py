# jason wilder

i = 0

while i < 1000:
    i += 1
    if i % 2 == 0:
        continue  # jump immediately to the while condition
    print(i, end=" ")


