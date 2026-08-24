class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init hash map, and then add numbers and occurences
        hash_map = dict()
        # init
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        #print(hash_map)
        # iterate through hashmap using hashmap keys, store in min heap for efficient replacement, and then keep top k largest
        return heapq.nlargest(k, hash_map, key=hash_map.get)