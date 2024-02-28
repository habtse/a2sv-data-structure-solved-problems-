class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        countVowels = 0
        left = 0
        for j in range(k):
            if s[j] in vowels:
                countVowels += 1
        result = countVowels
        for i in range(k,len(s)):
            if s[left] in vowels:
                countVowels -=1
            left += 1
            if s[i] in vowels:
                countVowels +=1
            result = max(result,countVowels)
        return result