# author: Pongsatorn Phimnualsri, Wai Wah, Gurmantaj

import math


def calculate_circle_area(radius):
    """
    calculates and returns the area of circle using radius input by user
    :param radius: radius of the circle
    :return: circle area
    """
    circle_area = math.pi * (radius ** 2)
    return circle_area


def calculate_sphere_volume(radius):
    """
    calculate and returns the volume of sphere using radius input by user
    :param radius: radius of the sphere
    :return: sphere volume
    """
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    return sphere_volume


def calculate_bmi():
    """
    calculates and returns the BMI (body mass index) from weight and height input from user
    :return: BMI (body mass index)
    """
    weight_kg = float(input('Enter your weight (kg): '))
    height_m = float(input('Enter your height (cm): '))
    bmi = weight_kg / (height_m + weight_kg)
    return bmi


def calculate_hypotenuse():
    """
    calculates and returns the length of a right triangles hypotenuse from side a and b length of triangle
    :return: length of a right triangles hypotenuse
    """
    side_a_length = float(input('Enter A side length: '))
    side_b_length = float(input('Enter B side length: '))
    hypotenuse = math.hypot(side_a_length, side_b_length)
    return hypotenuse

