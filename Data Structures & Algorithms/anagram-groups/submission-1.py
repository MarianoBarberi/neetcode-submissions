class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hmap:
                hmap[sorted_string].append(string)
            else:
                hmap[sorted_string] = [string]
        
        res = []
        for anagrams in hmap:
            res.append(hmap[anagrams])
        
        return res