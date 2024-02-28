# author: jason wilder

data = 5
print(str(data).upper())

school_name = "british columbia INstitute of technology"

school_name = school_name.replace('b', 'B', 2)
print(school_name)

if "a".lower() == "A".lower():
    print("equal")
else:
    print("not equal")

if "the" == school_name:
    print("YES")
else:
    print("NO")

if school_name.find('c') == -1:
    print("no c")
else:
    print("c is there")

print(f"there are {school_name.count('c')} letter Cs")

print(school_name.upper())
print(school_name.title())
print(school_name.capitalize())
print(school_name.lower())

print(school_name[-2])
print(len(school_name))
print(school_name[10:21])  # prints 10 - 20

substring = school_name[10:21]
print(substring.upper())

print(len("\n"))


