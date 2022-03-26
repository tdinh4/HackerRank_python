'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Parameter:
----------
    nums: List
        array of integers nums
    target: Int
        integer target

Return:
---------
    list: List
        return indices of the two numbers such that they add up to target

Example1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example3:
Input: nums = [3,3], target = 6
Output: [0,1]

Time: O(n^2)
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if ((nums[i]+nums[j]) == target):
                    result = [i,j]
        return result

if __name__ == '__main__':
    result = Solution()
    test_case = result.twoSum([2,7,11,15], 9)
    print(test_case)