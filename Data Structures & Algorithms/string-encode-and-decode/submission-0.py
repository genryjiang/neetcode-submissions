class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        len_words = list()
        # Len before
        for s in strs:
            len_words.append(len(s))
        # Convert list to string      
        for num in len_words:
            res += str(num)
            res += ','
        res += '#'        
        for word in strs:
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        # given s
        # read everything until the first #
        # find index of first #
        res = []
        print(s)
        index = s.find('#')
        info = s[:index]
        term = s[index + 1:]
        # convert info to list
        info_lst = [i for i in info.strip().split(",") if i]
        start = 0
        for i in info_lst:
            # taking i, grab the first i letters,
            end = start + int(i)
            word = term[start:end]
            start = end
            res.append(word)
        return res
