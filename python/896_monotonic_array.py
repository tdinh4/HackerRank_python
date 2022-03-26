'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Parameter:
----------
    nums: List
        List of integer array

Return:
---------
    bool: boolean
        true if the given array is monotonic, or false otherwise.

Example1:
Input: nums = [1,2,2,3]
Output: true

Example2:
Input: nums = [6,5,4,4]
Output: true

Example3:
Input: nums = [1,3,2]
Output: false

Time: O(n)
Space: 0(1)
'''
from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = descreasing = True
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                descreasing = False
            if nums[i] > nums[i+1]:
                increasing = False
        return increasing or descreasing

if __name__ == '__main__':
    result = Solution()
    test_case = result.isMonotonic([1,2,2,3])
    print(test_case)