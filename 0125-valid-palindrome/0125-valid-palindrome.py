class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = ''.join(char.lower() for char in s if char.isalnum())
        if only_letters == only_letters[::-1]:
            return True
        else: return False
