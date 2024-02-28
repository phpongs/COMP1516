# author: Pongsatorn Phimnualsri

try:
    score = float(input('Enter store: '))

    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'

        print(grade)
    else:
        print('Bad score. Please enter a score between 0.0 and 1.0')

except ValueError:
    print('Bad score. Please enter numeric value.')