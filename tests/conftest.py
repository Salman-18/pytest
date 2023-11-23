import pytest
import src.shapes as shapes
from src.school import ClassRoom, Teacher, Student
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def your_rectangle():
    return shapes.Rectangle(5, 6)

@pytest.fixture
def sample_classroom():
    teacher = Teacher(name="Professor Dumbledore")
    students = [Student(name=f"Student {i+1}") for i in range(10)]
    course_title = "Defense Against the Dark Arts"
    return ClassRoom(teacher, students, course_title)