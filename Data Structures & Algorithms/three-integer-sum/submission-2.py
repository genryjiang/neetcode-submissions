class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # how to filter out if i,j,k already exist
        # sort first
        nums.sort()
        left = 0
        right = len(nums)-1
        res = []
        print(nums)
        for i, num in enumerate(nums):
            # condition: if i != first, and nums[i] == nums [i-1] (dup val),
            # skip
            if i > 0 and nums[i] == nums[i-1]:
                continue;
            if num > 0:
                break
            # left and right are > 0 as i is fixed, idiot
            l,r = i+1, len(nums)-1
            while (l < r):
                threeSum = nums[l] + nums[r] + nums[i] 
                if (threeSum == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    # if valid, move both
                    l +=1
                    r -= 1
                    # duplicate check and skip
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if (threeSum > 0):
                    # too big, move r down
                    r -= 1
                if (threeSum < 0):
                    l += 1
        return res
                    
