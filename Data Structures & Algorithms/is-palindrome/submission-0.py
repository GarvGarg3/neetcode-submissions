class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for ch in s:
            if ch not in set("~!@#$%^&*()_+-={}|[]:\";'<>?,./` "):
                string += ch.lower()
        return string==string[::-1]