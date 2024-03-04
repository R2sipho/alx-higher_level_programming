#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_module_has_docstring(self):
        """Check if the module has a docstring."""
        module_docstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_docstring) > 1)

    def test_function_has_docstring(self):
        """Check if the max_integer function has a docstring."""
        function_docstring = max_integer.__doc__
        self.assertTrue(len(function_docstring) > 1)

    def test_empty_list_returns_none(self):
        """Test max_integer with an empty list, expecting None."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_no_args_returns_none(self):
        """Test max_integer with no arguments, expecting None."""
        result = max_integer()
        self.assertIsNone(result)

    def test_one_element_list(self):
        """Test max_integer with a list containing one element."""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_positive_max_at_end(self):
        """Test max_integer with positive numbers where the maximum is at the end."""
        result = max_integer([2, 10, 8, 36, 14, 50])
        self.assertEqual(result, 50)

    def test_positive_max_in_middle(self):
        """Test max_integer with positive numbers where the maximum is in the middle."""
        result = max_integer([2, 10, 8, 360, 14, 50])
        self.assertEqual(result, 360)

    def test_positive_max_at_beginning(self):
        """Test max_integer with positive numbers where the maximum is at the beginning."""
        result = max_integer([200, 10, 8, 36, 14, 50])
        self.assertEqual(result, 200)

    def test_one_negative_number(self):
        """Test max_integer with a list containing one negative number."""
        result = max_integer([200, 10, 8, -36, 14, 50])
        self.assertEqual(result, 200)

    def test_all_negative_numbers(self):
        """Test max_integer with a list containing all negative numbers."""
        result = max_integer([-6, -50, -75, -1, -100])
        self.assertEqual(result, -1)

    def test_passing_none_raises_type_error(self):
        """Test max_integer by passing None as an argument, expecting a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integer_in_list_raises_type_error(self):
        """Test max_integer with a list containing a non-integer type, expecting a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Hello", 4, 5])

if __name__ == "__main__":
    unittest.main()

