class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordHash = defaultdict(int)
        for word in s:
            wordHash[word] += 1

        for word in t:
            wordHash[word] -= 1

        for count in wordHash.values():
            if count != 0:
                return False
        return True