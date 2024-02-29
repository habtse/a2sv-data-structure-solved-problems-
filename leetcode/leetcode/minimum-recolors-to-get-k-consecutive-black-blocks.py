class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        left = 0
        result = window.count('W')
        for right in range(k,len(blocks)):
            left +=1
            result = min(blocks[left:right+1].count('W') , result)
        return result
            
