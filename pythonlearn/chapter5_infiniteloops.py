# author: Pongs

# copy till done 1
while True:
    line = input("input your words 1: ")
    if line == "done":
        break
    print(line)
print("Done!")

# copy till done 2
while True:
    line = input("input your words 2: ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")
