class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        sortedHash = defaultdict(list)

        for s in strs:
            sortedHash["".join(sorted(s))].append(s)

        finalList = []
        for keys in sortedHash:
            finalList.append(sortedHash[keys])

        return finalList