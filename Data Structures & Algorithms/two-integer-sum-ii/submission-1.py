class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # make two pointers: left and right (one at end, one at start)
        # always one valid solution: can terminate early
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if (sum > target):
                right -= 1
            if (sum < target):
                left += 1
            if (sum == target):
                break;
        # RETURN 1-indexed
        return [left+1, right+1]
