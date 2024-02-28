# author: Pongsatorn

# name input
Name = input('Enter your name: ')
print('Hello '+Name)

# hour and rate calculator
Hour = input('Enter Hours: ')
Hour = float(Hour)
Rate = input('Enter Rate: ')
Rate = float(Rate)
Pay = Hour * Rate
Pay = round(Pay)
print(Name+', your work ' + str(Hour) + ' hours at rate of ' + str(Rate) + ' $CA')
print('Your payment is ' + str(Pay) + ' $CA')

# celsius to fahrenheit
Celsius = float(input('Enter tempurature is celsius: '))
Fahrenheit = float(Celsius * 9/5) + 32
print(str(Celsius) + ' celsius is equal to ' + str(Fahrenheit) + ' fahrenheit')
