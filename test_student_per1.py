"""
TBSDrJ
Fall 2026
First example of a unit test.  NOTE: The first four letters of this
    filename MUST be 'test'.
"""
import unittest
import student_per1

class TestStudent(unittest.TestCase):
    """Tests for the Student class in student.py
    
    It is important that the first four letters of the class name
    are 'Test'."""
    def setUp(self):
        """Use setUp to create instances that you use in your tests."""
        self.alisa = student_per1.Student('Alisa', 'Timmerman')

    def test_str(self):
        """Testing the method __str__.
        
        Important that the name starts with 'test'."""
        self.assertIsInstance(str(self.alisa), str)
        self.assertIn(self.alisa.first_name, str(self.alisa))
        self.assertIn(self.alisa.last_name, str(self.alisa))

    def test_repr(self):
        """Testing the method __repr__."""
        alisa_clone = eval(f"student_per1.{repr(self.alisa)}")
        self.assertIsInstance(alisa_clone, student_per1.Student)
        self.alisa.grades.append(100)
        self.assertIn(100, self.alisa.grades)
        self.assertNotIn(100, alisa_clone.grades)

    def test_grades(self):

        # Alisa would never get less than 100%.
        if 'Alisa' == self.alisa.first_name:
            for grade in self.alisa.grades:
                self.assertGreaterEqual(grade, 100)