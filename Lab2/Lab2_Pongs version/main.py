# author: Pongsatorn Phimnualsri, Wai Wah, Gurmantaj

import utilities


def main():
    """
    set of functions from the utilities module including:
    - circle area calculator from radius input by user
    - sphere volume calculator from radius input by user
    - BMI calculator from weight(kg) and height input by user
    - hypotenuses calculator from the side a and b length input by user
    :return: results from each calculators
    """

    # circle area calculator
    radius = float(input('Enter the radius of a circle: '))
    print('The area of circle is ', utilities.calculate_circle_area(radius))

    # sphere volume calculator
    radius = float(input('Enter the radius of a sphere: '))
    print('The volume of the sphere is ', utilities.calculate_sphere_volume(radius))

    # BMI calculator
    print('The Body Mass Index is ', utilities.calculate_bmi())

    # hypotenuse calculator
    print('the hypotenuse length of the right triangle is: ', utilities.calculate_hypotenuse())


if __name__ == '__main__':
    main()
