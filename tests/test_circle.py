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
    def test_area(self):
        assert True 

