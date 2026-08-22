class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Setup hashmap
        hashMap = {}
        for i in nums:
            # initalise each number
            if hashMap.get(i) is None:
                # if not in, set value to 1
                hashMap[i] = 1
            # If present, +=1
            else:
                hashMap[i] += 1
        # Depending on k, return top k highest found
        return heapq.nlargest(k, hashMap, key=hashMap.get)