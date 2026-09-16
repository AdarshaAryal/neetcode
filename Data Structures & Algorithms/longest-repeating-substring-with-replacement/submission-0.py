class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        max_freq = 0

        l = 0
        N = len(s)
        count_map = collections.defaultdict(int)
        for r in range(N):
            count_map[s[r]] += 1
            max_freq = max(max_freq, count_map[s[r]])

            while (r - l + 1) - max_freq > k:
                count_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
