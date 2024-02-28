# authors: Pongsatorn Phimnualsri, Wai Wah Ng

import utilities


def main():
    """
    execute functions in the utilities modules to calculate area of circle, area of sphere,
    body-mass-index, and hypotenuse length of a right triangle
    :return: the calculated four items stated above
    """

    # calculation of circle area
    radius_cm = float(input("enter the radius of a circle in cm:"))
    print(" the area of circle is ", utilities.calculate_circle_area(radius_cm))

    # calculation of sphere volume
    radius_cm = float(input("enter the radius of a sphere in cm: "))
    print(" the volume of the sphere is: ", utilities.calculate_sphere_volume(radius_cm))

    # calculation of body-mass-index
    print(" the Body Mass Index is: ", utilities.calculate_bmi())

    # calculation of hypotenuse length of the right triangle
    print("the hypotenuse length of the right triangle is: ", utilities.calculate_hypotenuse())


if __name__ == "__main__":  # main guard
    main()
