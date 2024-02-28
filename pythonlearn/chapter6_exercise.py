# author: Pongs

# Slicing String
str = 'X-DSPAM-Confidence: 0.8475'
atpos = str.find(':')
value = float(str[atpos+2:])
print(value)
print(type(value))