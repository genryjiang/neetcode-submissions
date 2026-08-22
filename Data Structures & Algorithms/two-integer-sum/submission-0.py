class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key, pair 
        # index, value
        pahanGay = {}
        for i, element in enumerate(nums):
        # TARGET - x = what? --> does that exist in hashmap
            if (target - element) in pahanGay:
                return [pahanGay[target-element], i]
            pahanGay[element] = i    
    
