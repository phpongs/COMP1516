# author: Pongs

word = 'banana potato'
count = 0

for letter in word:
    if letter == 'a':
        count += 1

print(count)

word = 'banana potato'

if word == 'banana potato':
    print('All right, Minion.')

if word < 'banana potato':
    print('Give me some ' + word + ' and you will be yellow.')
elif word > 'banana potato':
    print('Get away ' + word + ' you fucking Minion.')
else:
    print('All right, one eye')

stuff = 'hello world'
stuff = stuff.upper()
print(stuff)

index = stuff.find('WO')
print(index)


line = ' Here we go '
line = line.strip()
print(line)

fruit = 'banana'
fruit_count = fruit.count('a')
print(fruit_count)

camels = 42
f'{camels}'
