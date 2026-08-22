class Solution:

    def encode(self, strs: List[str]) -> str:
        # list of strings, need to combine
        # for each word, add length and a unique identifier (#) to specify length to separate
        if not strs:
            return  ""
        combined = ""
        for word in strs:
            combined += str(len(word)) + "#" + word
        print(combined)
        return combined


    def decode(self, s: str) -> List[str]:
        # empty list to add to after decoding
        res = []
        # i counter to find length
        # j 
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res