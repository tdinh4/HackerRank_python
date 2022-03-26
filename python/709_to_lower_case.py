'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Parameter:
----------
    s: string

Return:
---------
    s: string
        string after replacing every uppercase with the same lowercase 

Example1:
Input: s = "Hello"
Output: "hello"

Example2:
Input: s = "here"
Output: "here"

Example3:
Input: s = "LOVELY"
Output: "lovely"

Time: O(1)
Space: O(1)
'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

if __name__ == '__main__':
    result = Solution()
    example_1 = result.toLowerCase("Hello")
    example_2 = result.toLowerCase("here")
    example_3 = result.toLowerCase("LOVELY")
    print(example_1,example_2,example_3)