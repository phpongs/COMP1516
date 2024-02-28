# jason wilder

# j:   0   1  2  3
nums = [1, 2, 5, 0]

# j:       0    1     2
letters = ['a', 'z', 'e']

# j:      0         1
names = ['tiger', 'bill']

# i:    data[0]  data[1]  data[2]
data = [nums, letters, names]
print(len(data))

i = 0
while i < len(data):
    one_list = data[i]  # e.g. first run: one_list == nums
    j = 0
    while j < len(one_list):
        print(one_list[j], end= " ")
        j += 1
    print("\n----------")
    i += 1

