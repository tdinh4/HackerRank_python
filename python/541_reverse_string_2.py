'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Parameter:
----------
    s: str
    k int

Return:
---------
    s: str

Example1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example2:
Input: s = "abcd", k = 2
Output: "bacd"

Example3:

Time: O(n)
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        sList = list(s)
        for i in range(0, len(s), 2*k):
            sList[i:i+k] = reversed(sList[i:i+k])
            result = ''.join(sList)
        return result

if __name__ == '__main__':
    result = Solution()
    test_case = result.reverseStr("abcdefg", 2)
    print(test_case)