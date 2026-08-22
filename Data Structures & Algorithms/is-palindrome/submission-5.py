class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # remove all spaces in a string
        # lowercase
        import re
        p = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        p = p.lower().replace(" ", "")
        print(p)
        i = 0
        # 0 indexed
        j = len(p) - 1
        while i <= j:
            if p[i] != p[j]:
                return False
            i += 1
            j -= 1
        return True