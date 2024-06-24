# tests/test_solution.py
import unittest
from solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_2(self):
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_all_positive(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

    def test_all_negative(self):
        self.assertEqual(self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6])

    def test_single_zero(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 0, 4]), [0, 0, 0, 24, 0])

    def test_multiple_zeros(self):
        self.assertEqual(self.solution.productExceptSelf([1, 0, 3, 0, 4]), [0, 0, 0, 0, 0])

    def test_large_numbers(self):
        self.assertEqual(self.solution.productExceptSelf([10, 20, 30, 40, 50]), [1200000, 600000, 400000, 300000, 240000])

    def test_two_elements(self):
        self.assertEqual(self.solution.productExceptSelf([2, 3]), [3, 2])

    def test_maximum_constraints(self):
        nums = [1] * 105
        self.assertEqual(self.solution.productExceptSelf(nums), [1] * 105)

    def test_minimum_constraints(self):
        nums = [1, 2]
        self.assertEqual(self.solution.productExceptSelf(nums), [2, 1])

    def tearDown(self):
        del self.solution

if __name__ == '__main__':
    unittest.main()
