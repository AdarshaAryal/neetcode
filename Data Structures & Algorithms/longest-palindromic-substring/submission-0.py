class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = "ababd"
        N = len(s)
        # N = 5
        def expand(l, r): # expand(l, 1)
            while l >= 0 and r < N and s[l] == s[r]: # l = 1, r = 1
                l -= 1 # l = -1
                r += 1 # r = 3
            return s[l + 1:r] # s[0]
        
        max_string = ""
        for index in range(N): 
            odd_max = expand(index, index) # odd_max = expand(1, 1)
            even_max = expand(index, index + 1) # even_max = expand(1, 2)
            max_string = max(max_string, odd_max, even_max, key = len) # max_string = "a"
        
        return max_string # max_string = 

        