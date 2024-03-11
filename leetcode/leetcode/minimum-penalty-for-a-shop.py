class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_sum = [0]
        for i in range(len(customers)):
            if customers[i] == "N":
                prefix_sum.append(1+prefix_sum[i])
            else:
                prefix_sum.append(prefix_sum[i])
        suffix_sum = [0]
        ptr = 0
        for j in range(len(customers)-1,-1,-1):
            if customers[j] == "Y":
                suffix_sum.append(1+suffix_sum[ptr])
            else:
                suffix_sum.append(suffix_sum[ptr])
            ptr += 1
        
        minm = float('inf')
        ans = -1
        for k in range(len(customers)+1):
            result = prefix_sum[k] + suffix_sum[len(customers)-k]
            if result < minm:
                ans = k
                minm = result
        return ans
