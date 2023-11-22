import pytest
import src.shapes as shapes
import math
class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}")
        self.cicrle = shapes.Circle(10)
    
    def teardown_method(self, method):
        print(f"teardown down {method}")

    def test_area(self):
        assert self.cicrle.area == math.pi * self.cicrle.radius ** 2
    
    def test_perimeter(self):
        result = self.cicrle.perimeter()
        expected = 2 * math.pi * self.cicrle.perimeter
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.cicrle.area() != my_rectangle.area()


