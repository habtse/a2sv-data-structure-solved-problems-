class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for k in range(len(image)):
            output.append([0]*len(image))
        for i in range( len(image)):
        
            for j in range(len(image)):
                if image[i][j] ==0:
                    output[i][len(image[i])-1-j] = 1
                else:
                    output[i][len(image[i])-1-j] = 0
        return output

