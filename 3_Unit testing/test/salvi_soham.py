#: Name: Salvi Patel
#: Name: Soham Patel
#: Date: June 18, 2023
#: Program name: area_finder
#: Description: This will test the area of four shapes as per the input


import unittest
from math import pi
import math
from app.salvi_soham import areaOfCircle, areaOfTrapezium, areaOfEllipse, areaOfRhombus


# Test Cases for Circle Area
class TestForCircle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    def setUp(self):
        print("setup")

    def test_trueRadius(self):
        radius = 5
        area = areaOfCircle(radius)
        self.assertAlmostEqual(area, math.pi * radius ** 2)
        print("End of test: Test areas when radius of circle >= 0")

    def test_negativeRadius(self):
        radius = -5
        with self.assertRaises(ValueError) as cm:
            areaOfCircle(radius)
        self.assertEqual(str(cm.exception), "Radius must be a non-negative number and should be greater than or equals to 0")
        print("End of test: Exception raised when radius of circle < 0")

    def test_wrongRadius(self):
        with self.assertRaises(TypeError):
            areaOfCircle("invalid")
        print("End of test: Exception raised when radius of circle is an invalid type")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")


# Test Cases for Trapezium Area
class TestForTrapezium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    def setUp(self):
        print("setup")

    def test_trueHeight(self):
        A1 = 3
        B1 = -3
        height = -0
        area = areaOfTrapezium(A1, B1, height)
        self.assertEqual(area, 15)
        print("End of test: Test areas when bases and height of trapezium >= 0")

    def test_negativeHeight(self):
        with self.assertRaises(ValueError) as cm:
            areaOfTrapezium(-3, 6, 3)
        self.assertEqual(str(cm.exception), "Base and height must be non-negative numbers and should be greater than or equals to 0")
        print("End of test: Exception raised when bases or height of trapezium < 0")

    def test_wrongInput(self):
        with self.assertRaises(TypeError):
            areaOfTrapezium("invalid", 6, 3)
        print("End of test: Exception raised when non-numeric or invalid input entered")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")


# Test Cases for Ellipse Area
class TestForEllipse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    def setUp(self):
        print("setup")

    def test_trueAxis(self):
        axis1 = 2
        axis2 = -2
        area = areaOfEllipse(axis1, axis2)
        self.assertAlmostEqual(area, pi * axis1 * axis2)
        print("End of test: Test areas when semi-major and semi-minor axes of ellipse >= 0")

    def test_negativeAxis(self):
        with self.assertRaises(ValueError) as cm:
            areaOfEllipse(-3, 2)
        self.assertEqual(str(cm.exception), "Every semi-major and semi-minor axis must be non-negative numbers and should be greater than or equals to 0")
        print("End of test: Exception raised for negative or zero semi-axes")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")


# Test Cases for Rhombus Area
class TestForRhombus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    def setUp(self):
        print("setup")

    def test_trueDiagonal(self):
        d1 = 1
        d2 = -2
        area = areaOfRhombus(d1, d2)
        self.assertEqual(area, 12)
        print("End of test: Test areas when diagonals of rhombus >= 0")

    def test_wrongDiagonal(self):
        with self.assertRaises(ValueError) as cm:
            areaOfRhombus(-3, 6)
        self.assertEqual(str(cm.exception), "Both diagonals must be non-negative numbers and should be greater than or equals to 0")
        print("End of test: Exception raised for negative diagonal")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")


def main():
    while True:
        print("\nPlease enter one of the following options:")
        print("'c' for testing area of circle")
        print("'t' for testing area of trapezium")
        print("'e' for testing area of ellipse")
        print("'p' for testing area of rhombus")
        print("'q' to quit")

        optionsToChoose = input("What would you like to do? ")

        if optionsToChoose.lower() == 'c':
            suite = unittest.TestLoader().loadTestsFromTestCase(TestForCircle)
            runner = unittest.TextTestRunner()
            result = runner.run(suite)
            print(result)
        elif optionsToChoose.lower() == 't':
            suite = unittest.TestLoader().loadTestsFromTestCase(TestForTrapezium)
            runner = unittest.TextTestRunner()
            result = runner.run(suite)
            print(result)
        elif optionsToChoose.lower() == 'e':
            suite = unittest.TestLoader().loadTestsFromTestCase(TestForEllipse)
            runner = unittest.TextTestRunner()
            result = runner.run(suite)
            print(result)
        elif optionsToChoose.lower() == 'p':
            suite = unittest.TestLoader().loadTestsFromTestCase(TestForRhombus)
            runner = unittest.TextTestRunner()
            result = runner.run(suite)
            print(result)
        elif optionsToChoose.lower() == 'q':
            break
        else:
            print("Invalid options. Please try again.")


if __name__ == '__main__':
    main()
