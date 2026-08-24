class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for i in range(len(s)):
            if s[i] in hmap:
                hmap[s[i]] += 1
            else:
                hmap[s[i]] = 1
        
        hmap2 = {}
        for j in range(len(t)):
            if t[j] in hmap2:
                hmap2[t[j]] += 1
            else:
                hmap2[t[j]] = 1

        if hmap == hmap2:
            return True
        return False