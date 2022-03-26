'''
Given an array nums of integers, return how many of them contain an even number of digits.

Parameter:
----------
    nums: List
        array nums of integers

Return:
---------
    count: Int
        how many of them contain an even number of digits.

Example1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Example3:

Time: O(n)
Space: O(1)
'''
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if (len(str(i)) % 2 == 0):
                result += 1
        return result

if __name__ == '__main__':
    result = Solution()
    test_case = result.findNumbers([12,345,2,6,7896])
    print(test_case)