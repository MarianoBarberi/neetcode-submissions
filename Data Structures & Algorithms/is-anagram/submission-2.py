class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l1, l2 = [], []
        for char, char2 in zip(s,t):
            l1.append(char)
            l2.append(char2)

        if sorted(l1) == sorted(l2):
            return True
        return False