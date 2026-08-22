class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string, sort and add to hash map
        hash_map = defaultdict()
        for word in strs:
            # make key value sorted string
            res = "".join(sorted(word))
            # if not in, we will then add
            if res not in hash_map:
                hash_map[res] = []
            # if in, add that shi
            hash_map[res].append(word)
        # Return all values as a list of list
        return list(hash_map.values())

            