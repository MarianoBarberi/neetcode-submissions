class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join([char for char in s if char.isalnum()]).lower()
        print(filtered_s) 
        print(filtered_s[::-1])
        if filtered_s[::-1] == filtered_s:
            return True
        return False