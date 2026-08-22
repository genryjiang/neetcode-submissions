class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)
    # Make a
        for i in strs:
            freq = [0]*26
            # Extract freq of letters
            for j in i:
                index = ord(j.lower()) - ord('a')
                freq[index] += 1
            # push the letter to this freq in hash map
            hashMap[tuple(freq)].append(i)
        return list(hashMap.values())

        