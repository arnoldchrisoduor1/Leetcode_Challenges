import unittest
from twosum import Solution


class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        nums = [5, 8, 9, 3]
        target = 8
        expected_result = [0, 3]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

        nums = [6, 8, 4]
        target = 10
        expected_result = [0, 2]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

        nums = [7, 4]
        target = 11
        expected_result = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
