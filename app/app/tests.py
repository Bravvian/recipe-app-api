""""
Sample test file

"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
  """Test the calc module."""

  def test_add_numbers(self):
    """Test adding numbers together."""
    self.assertEqual(calc.add(4,5), 9)


  def test_subtract_numbers(self):
    """Test subtracting numbers."""
    self.assertEqual(calc.subtract(10,5), 5)

