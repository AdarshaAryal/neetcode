class Solution:
    def trap(self, height: List[int]) -> int:
        # get left_max and right_max of the position
        # water trapped = min(left, right) - height[i]
        # start shifting pointer to the max part
        # two pointer problem
        # Time complexity: O(n)
        # Space complexity: O(n) -> O(1) optimise 
        # height = [0,2,0,3,1,0,1,3,2,1]
        N = len(height)
        lptr = 1
        rptr = N - 2
        left_max = [0] * N
        right_max = [0] * N
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        
        while lptr < N:
            left_max[lptr] = max(left_max[lptr-1], height[lptr])
            lptr += 1
            right_max[rptr] = max(right_max[rptr+1], height[rptr])
            rptr -= 1
        
        res = 0

        for i in range(N):
            cur_water = min(left_max[i], right_max[i]) - height[i]
            res += cur_water

        return res 
                