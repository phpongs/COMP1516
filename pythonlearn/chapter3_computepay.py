# author: Pongsatorn Phimnualsri

name = input('Enter your name: ')

try:
    hour = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if hour > 40:
        overtime = hour - 40
        overtime_rate = rate * 1.5
        overtime_pay = overtime * overtime_rate
        regular_pay = 40 * rate
        pay = regular_pay + overtime_pay
    else:
        pay = hour * rate
    print('Pay:', round(pay, 2))

except ValueError:
    print('Error, please enter numeric input')
