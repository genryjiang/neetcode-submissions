class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map setup for O(n) lookup
        hash_map = dict()
        for i,n in enumerate(nums):
            # target - x = unknown number, if this number exists, twosum is complete
            if (target - n) in hash_map:
                # if found, return this in a tuple format
                return [hash_map[target-n], i]
                # If not found, add to the hashmap
            hash_map[n] = i