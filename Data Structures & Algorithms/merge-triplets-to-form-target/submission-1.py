class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for val in triplets:
            if val[0] > target[0] or val[1] > target[1] or val[2] > target[2]:
                # skip these values
                continue;
            for i, v in enumerate(val):
                if v == target[i]:
                    res.add(i);
        # return true if the lenght is 3, everything else is bad (more, less)
        return len(res) == 3;
        