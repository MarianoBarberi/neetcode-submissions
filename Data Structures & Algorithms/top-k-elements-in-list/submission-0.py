class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        final_list = []
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        for i in range(k):
            value = max(hmap, key=hmap.get)
            del hmap[value]
            final_list.append(value)
        return final_list