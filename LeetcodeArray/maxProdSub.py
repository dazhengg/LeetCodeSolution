class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        i = 0
        currentMax, currentMin, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)): 
            n = nums[i] #[3] now #[-2]
            tmp = currentMax #[3], now #[6]
            currentMax = max(n, n*currentMax, n*currentMin)  #[3*2]
            currentMin = min(n, n*tmp, n*currentMin) #[-12] (find the best negative))
            ans = max(ans, currentMax) #[3,2]
        return ans
    
# https://www.youtube.com/watch?v=vtJvbRlHqTA 
#Maximum Product Subarray (contiguous subarray within an array)