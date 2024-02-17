class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len (palindrome)==1:
            return ''
        listP = list(palindrome)
        for i in range(ceil(len(listP)/2)):
            if ceil(len(listP)/2) -1  == i and listP[i] != 'a' and len(listP)%2 ==1 :
                continue
            if listP[i] != 'a':
                listP[i] = 'a'
                return ''.join(listP)
        listP[len(listP)-1] = 'b'
        return ''.join(listP)

