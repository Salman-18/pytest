import pytest
import src.shapes as shapes
from src.school import ClassRoom, Teacher, Student

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def your_rectangle():
    return shapes.Rectangle(5, 6)

