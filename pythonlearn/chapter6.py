# author: Pongs

fruit = 'banana'
letter = fruit[1]
print(letter)

fruit[:]

length = len(fruit)
print(length)

last = fruit[length-1]
print(last)
print('')

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter, end=' ')
    index = index + 1

print()

for char in fruit:
    print(char, end=' ')
