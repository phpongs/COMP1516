# jason wilder
# index:        0         1      2      3      4
languages = ['python', 'java', 'c++', 'php', 'swift']

print(languages)
popped = languages.pop(2)         # pop by index
languages[3] = None
print("i just popped " + popped)
languages.remove('php')  # remove by value
del languages[0]         # delete by index
print(languages)
