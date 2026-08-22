class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fuck_you_pahan = {}
        for i in s:
            if i not in fuck_you_pahan:
                fuck_you_pahan[i] = 1
            else:
                fuck_you_pahan[i] += 1 
        for j in t:
            if j in fuck_you_pahan:
                fuck_you_pahan[j] -= 1
            else:
                fuck_you_pahan[i] = 1
             
        for value in fuck_you_pahan.values():
            if value != 0:
                return False
        return True