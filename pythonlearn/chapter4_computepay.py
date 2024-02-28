# author: Pongsatorn

Hour = input('Enter Hours: ')
Hour = float(Hour)
Rate = input('Enter Rate: ')
Rate = float(Rate)
Pay = Hour * Rate
Pay = round(Pay)

def computepay(Hour, Rate):
    multiple = (Hour * Rate)
    return multiple

x = computepay(Hour, Rate)
print(x)