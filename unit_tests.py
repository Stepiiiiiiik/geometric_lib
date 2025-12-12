import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestRectangle(unittest.TestCase):
    def test_area_correct_values(self):
        self.assertEqual(rect_area(15, 11), 165)

    def test_area_zero_value(self):
        self.assertEqual(rect_area(0, 10), 0)

    def test_area_negative_value(self):
        self.assertEqual(rect_area(5, -10), 50)

    def test_perimeter_correct_value(self):
        self.assertEqual(rect_perimeter(5, 10), 30)

    def test_perimeter_zero_value(self):
        self.assertEqual(rect_perimeter(0, 10), 20)


class TestSquare(unittest.TestCase):
    def test_area_correct_value(self):
        self.assertEqual(square_area(5), 25)

    def test_area_zero_value(self):
        self.assertEqual(square_area(0), 0)

    def test_perimeter_correct_value(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_perimeter_zero_value(self):
        self.assertEqual(square_perimeter(0), 0)


class TestTriangle(unittest.TestCase):
    def test_area_correct_value(self):
        self.assertEqual(triangle_area(3, 4), 6)

    def test_area_zero_value(self):
        self.assertEqual(triangle_area(0, 4), 0)

    def test_area_negative_value(self):
        self.assertEqual(triangle_area(-3, 4), 6)

    def test_perimeter_correct_value(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_perimeter_zero_value(self):
        self.assertEqual(triangle_perimeter(0, 4, 1), 5)

    def test_perimeter_negative_value(self):
        self.assertEqual(triangle_perimeter(-3, 4, 1), 8)


class TestCircle(unittest.TestCase):
    def test_area_correct_value(self):
        self.assertAlmostEqual(circle_area(5), 78.54, places=2)

    def test_area_zero_value(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_negative_value(self):
        self.assertAlmostEqual(circle_area(-5), 78.54, places=2)

    def test_perimeter_normal_value(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.42, places=2)

    def test_perimeter_zero_value(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_perimeter_negative_value(self):
        self.assertAlmostEqual(circle_perimeter(-5), 31.42, places=2)

if __name__ == "__main__":
    unittest.main()
