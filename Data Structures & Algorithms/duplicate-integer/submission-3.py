class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # Create hash table
       # Add numbers to hash table and keep count
       # if a key has a value of more than 2, return true
       # else, return false

        num_table = dict()
        # Add numbers to hash table --> cycle thru list
        for num in nums:
            # if not in dict, add
            if num not in num_table:
                num_table[num] = 1;
            # if in table, increment counter
            else:
                num_table[num] += 1;
        # Check 
            if list(num_table.values()).count(2) >= 1:
                return True
                
        return False