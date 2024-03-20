class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count= Counter(words)
        ans = defaultdict(set)
        for word in words:
            ans[count[word]].add(word)
        vals = sorted(ans.keys(),reverse=True)

        res = []
        for key in vals:
            res += sorted(list(ans[key]))
            if len(res) >= k:
                return res[:k]
