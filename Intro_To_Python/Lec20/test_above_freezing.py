import unittest
import temperature


class TestAboveFreezing(unittest.TestCase):  # inheritance
    """Tests for temperature.above_freezing."""

    def test_above_freezing_above(self):
        """Test a temperature that is above freezing."""
        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual, "The temperature is above freezing.")  # assertEqual: test a statement

    def test_above_freezing_below(self):
        """Test a temperature that is below freezing."""
        expected = False
        actual = temperature.above_freezing(-2)
        self.assertEqual(expected, actual, "The temperature is below freezing.")

    def test_above_freezing_at_zero(self):
        """Test a temperature that is at freezing."""
        expected = False
        actual = temperature.above_freezing(0)
        self.assertEqual(expected, actual, "The temperature is at the freezing mark.")


if __name__ == '__main__':
    unittest.main()
    # execute every method beginning with test
