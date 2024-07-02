#: Name: Salvi Patel
#: Name: Soham Patel
#: Date: June 18, 2023
#: Program name: area_finder
#: Description: This will test the area of four shapes as per the input


from math import pi
import unittest
import math


# Function to calculate the area of a circle
def areaOfCircle(r):
    if r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Radius must be a non-negative number and should be greater than or equals to 0")


# Function to calculate the area of a trapezium
# A1 = base 1 and B1 = base 2
def areaOfTrapezium(A1, B1, height):
    if A1 >= 0 and B1 >= 0 and height >= 0:
        return 0.5 * (A1 + B1) * height
    else:
        raise ValueError("Base and height must be non-negative numbers and should be greater than or equals to 0")


# Function to calculate the area of an ellipse
def areaOfEllipse(axis1, axis2):
    if axis1 >= 0 and axis2 >= 0:
        return pi * axis1 * axis2
    else:
        raise ValueError("Every semi-major and semi-minor axes must be non-negative numbers and should be greater than or equals to 0")


# Function to calculate the area of a rhombus
def areaOfRhombus(d1, d2):
    if d1 >= 0 and d2 >= 0:
        return 0.5 * d1 * d2
    else:
        raise ValueError("Both diagonals must be non-negative numbers and should be greater than or equals to 0")