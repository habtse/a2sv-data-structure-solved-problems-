class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''
        for i in s:
            if not i.isalnum():
                continue
            else:
                alphanumeric +=i.lower()
        for i in range (len(alphanumeric)//2):
            if alphanumeric[i] != alphanumeric[len(alphanumeric)-i-1]:
                return False
        return True
