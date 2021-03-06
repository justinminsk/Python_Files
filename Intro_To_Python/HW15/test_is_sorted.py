import is_sorted as is_sorted
import unittest


class Test_list_mag(unittest.TestCase):

    def test_list_mag_empty(self):  # 1
        """Test an empty list."""
        argument = []
        expected = True
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_running_list_mag_item(self):  # 2
        """Test a one-item list."""
        argument = [5]
        expected = True
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_running_list_mag_items(self):  # 3
        """Test a two-item list."""
        argument = [5, 2]
        expected = False
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_list_mag_negative(self):  # 4
        """Test a list of negative values."""
        argument = [-1, -5, -3, -4]
        expected = False
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list contains only negative values.")

    def test_running_list_mag_zeros(self):  # 5
        """Test a list of zeros."""
        argument = [0, 0, 0, 0]
        expected = True
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list contains only zeros.")

    def test_running_list_mag_positive(self):  # 6
        """Test a list of positive values."""
        argument = [4, 2, 3, 6]
        expected = False
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list contains only positive values.")

    def test_running_list_mag_mix(self):  # 7
        """Test a list containing mixture of negative values, zeros and positive values."""
        argument = [-5, -2, 0, 1, 3, 4]
        expected = True
        argument = is_sorted.is_sorted(argument)
        self.assertEqual(expected, argument, "The list contains a mixture of negative values, zeros and positive values"
                                             ".")


if __name__ == '__main__':
    unittest.main()