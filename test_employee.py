import unittest
from employee import Employee  

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Create an employee instance to use in tests."""
        self.cally = Employee("callum", "gordon", 400)

    def test_give_default_raise(self):
        """Test that a default raise adds 5000."""
        self.cally.give_raise()
        self.assertEqual(self.cally.annual_salary, 5400)

    def test_give_custom_raise(self):
        """Test that a custom raise amount works correctly."""
        self.cally.give_raise(20000)
        self.assertEqual(self.cally.annual_salary, 20400)

if __name__ == '__main__':
    unittest.main()