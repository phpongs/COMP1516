# author: Pongsatorn Phimnualsri

inp = input('Enter Fahrenheit Tempurature:')
try:
    fah = float(inp)
    cel = (fah - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Use only number!')
