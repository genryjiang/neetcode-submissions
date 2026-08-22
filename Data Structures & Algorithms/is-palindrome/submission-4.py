import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # regex
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if (s[::-1] != s):
            return False
        return True

