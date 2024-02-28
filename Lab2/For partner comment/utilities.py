# authors: Pongsatorn, Wai Wah Ng, Gurmantaj

import math


def calculate_circle_area(radius_cm):
    """
    calculate circle area based on radius
    :param radius_cm: radius of a circle
    :return: circle area in cm^2
    """
    return float(math.pi * radius_cm ** 2)


def calculate_sphere_volume(radius_cm):
    """
    calculate sphere volume based on radius
    :param radius_cm: radius of a sphere
    :return: volume of a sphere in cm^3
    """
    return float(4 / 3 * math.pi * radius_cm ** 3)


def calculate_bmi():
    """
    prompt user input the height in kg and height in meter and then calculate body mass index
    :return: body mass index
    """
    weight_kg = float(input("enter the weight in kilograms: "))
    height_meters = float(input("enter the height in meters: "))
    bmi = weight_kg / height_meters ** 2
    return bmi


def calculate_hypotenuse():
    """
    prompts the user to enter lengths of sides A and B of a right triangle. Then calculate and
    return the length of a right triangles hypotenuse
    :return: length of a right triangles hypotenuse
    """
    side_a_cm = float(input("enter the length of side A in cm: "))
    side_b_cm = float(input("enter the length of side B in cm: "))
    return math.hypot(side_a_cm, side_b_cm)
