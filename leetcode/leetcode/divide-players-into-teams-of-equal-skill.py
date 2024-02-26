class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        if len(skill) % 2 ==1:
            return -1
        first = skill[0]+skill[-1]
        total =0
        for i in range(len(skill)//2):
            if first != skill[i]+skill[len(skill)-1-i]:
                return -1
            else:
                total += (skill[i]*skill[len(skill)-1-i])
        return total 
