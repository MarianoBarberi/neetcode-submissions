class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numHash = defaultdict(int)
        finalList = []
        for num in nums:
            numHash[num] += 1

        for i in range(k):
            maxVal = 0
            tempKey = 0
            for key in numHash:
                if maxVal < numHash[key]:
                    maxVal = numHash[key]
                    tempKey = key
            numHash[tempKey] = 0
            finalList.append(tempKey)
        return finalList
        
        