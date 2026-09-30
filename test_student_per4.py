"""
TBSDrJ
Fall 2026
Unit tests for the Student class.  It is important that the name of this
    file starts with "test".
"""
import unittest
import student_per4

class TestStudent(unittest.TestCase):
    """Unit tests for the Student class from student.py.
    
    It is important that the name of this class starts with 'Test'."""
    def setUp(self):
        """This is built in to unittest library, runs before every test."""
        self.tomas = student_per4.Student('Tomas', 'Bejar')

    def tearDown(self):
        """Runs after each test.s"""

    def test_init(self):
        """Test the __init__ method.
        
        It is important that the name starts with 'test'."""
        self.assertIsInstance(self.tomas.first_name, str)
        self.assertIsInstance(self.tomas.last_name, str)
        self.assertIsInstance(self.tomas.grades, list)

    def test_str(self):
        self.assertIsInstance(str(self.tomas), str)
        self.assertLess(len(str(self.tomas)), 70)

    def test_repr(self):
        self.assertIsInstance(str(self.tomas), str)
        self.assertIsInstance(eval(f"student_per4.{repr(self.tomas)}"), 
                student_per4.Student)
    