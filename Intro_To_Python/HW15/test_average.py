import average as avg
import unittest


class Test_list_mag(unittest.TestCase):

    def test_running_list_mag_item(self):  # 2
        """Test a one-item list."""
        argument = [5]
        expected = 5
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_running_list_mag_items(self):  # 3
        """Test a two-item list."""
        argument = [5, 2]
        expected = 3.5
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_list_mag_negative(self):  # 4
        """Test a list of negative values."""
        argument = [-1, -5, -3, -4]
        expected = -3.25
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains only negative values.")

    def test_running_list_mag_zeros(self):  # 5
        """Test a list of zeros."""
        argument = [0, 0, 0, 0]
        expected = 0
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains only zeros.")

    def test_running_list_mag_positive(self):  # 6
        """Test a list of positive values."""
        argument = [None, 2, 3, 6]
        expected = 3.6666666666666665
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains positive values and None.")

    def test_running_list_mag_mix(self):  # 7
        """Test a list containing mixture of negative values, zeros and positive values."""
        argument = [-5, -2, 0, 1, 3, 4]
        expected = 0.16666666666666666
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains a mixture of negative values, zeros and positive values"
                                             ".")

    def test_running_list_mag_mix(self):  # 7
        """Test a list containing mixture of negative values, zeros and positive values."""
        argument = [-5, None, -2, 0, 1, 3, 4, None]
        expected = 0.16666666666666666
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list contains a mixture of negative values, zeros, None, and positive"
                                             " values.")


if __name__ == '__main__':
    unittest.main()