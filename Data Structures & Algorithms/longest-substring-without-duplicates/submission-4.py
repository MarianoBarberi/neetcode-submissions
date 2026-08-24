class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        char_list = []
        max_value = 0
        while r < len(s):
            if s[r] not in char_list:
                char_list.append(s[r])
            else:
                char_list = char_list[char_list.index(s[r])+1:]
                char_list.append(s[r])
                l = s.index(char_list[0])
            r += 1
            max_value = max(max_value, len(char_list))
        return max_value