# jason wilder

trait = input("name a good habit: ")

f = open("success.txt", "a")
f.write(f"{trait}\n")
f.close()

with open("success.txt", "r") as file:
    list_of_lines = file.readlines()

for one_line in list_of_lines:
    print(one_line.upper(), end="")
