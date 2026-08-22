class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # begin: check if same len
        if len(s) != len(t):
            return False
        # Hashmap
        map_s = dict()
        map_t = dict();
        # add all of S into dict, and add count
        for letter in s:
            if letter not in map_s:
                map_s[letter] = 1
            else:
                map_s[letter] += 1
        # Now add t to map_t
        for t_char in t:
            if t_char not in map_t:
                map_t[t_char] = 1
            else:
                map_t[t_char] += 1;
        if map_s == map_t:
            return True
        return False