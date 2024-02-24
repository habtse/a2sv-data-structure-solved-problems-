class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic ={}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        output =deque([])
        print(sorted(dic.items()))
        for key,value in sorted(dic.items()):
            output.appendleft(value)
        print(output)
        return output

