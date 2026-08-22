import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        # for int i = 0; i < len(s); i++ 
            # go from end, go and go from start
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True