class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1

        res = []
        for i in range(k):
            val = max(hmap, key=hmap.get)
            res.append(val)
            hmap[val] = 0
        return res