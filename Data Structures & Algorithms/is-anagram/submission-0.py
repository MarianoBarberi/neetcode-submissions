class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap, hmap2 = {}, {}
        for letter in s:
            if letter in hmap:
                hmap[letter] += 1
            else:
                hmap[letter] = 1
        for char in t:
            if char in hmap2:
                hmap2[char] += 1
            else:
                hmap2[char] = 1
        if hmap == hmap2:
            return True
        else:
            return False