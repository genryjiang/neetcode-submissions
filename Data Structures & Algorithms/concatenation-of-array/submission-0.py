class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lengthList = []
        # nums[i] == nums[i+1]
        count = 0
        for i in range(2):
            for j in nums:
                lengthList.append(j)
        return lengthList