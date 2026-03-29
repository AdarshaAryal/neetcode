class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        
        def is_palindrome(l, r):   
            while l < r:
                if not s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        res = []
        def backtrack(index, cur_path):
            
            if index == N:
                res.append(cur_path[:])
                return
            for i in range(index, N):
                if is_palindrome(index, i):
                    cur_path.append(s[index: i + 1])
                    backtrack(i + 1, cur_path)
                    cur_path.pop()
        
        backtrack(0, [])
        return res


            