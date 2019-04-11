#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.

#https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 1)[::-1]:
            print(i)
            if i + nums[i] >= goal:
                goal = i
        return not goal
