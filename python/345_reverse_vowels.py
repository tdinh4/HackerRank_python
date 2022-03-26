'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Parameter:
----------
    s: str

Return:
---------
    s: str
        return reverse only all the vowels
    

Example1:
Input: s = "hello"
Output: "holle"

Example2:
Input: s = "leetcode"
Output: "leotcede"

Example3:

Time: O(n)
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ''
        vowels = 'aeiou'
        left = 0
        right = len(s) - 1
        sList = list(s)
        while (left <= right):
            if sList[left] not in vowels:
                left += 1
            elif sList[right] not in vowels:
                right -= 1
            else:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
        result = ''.join(sList)
        return result

if __name__ == '__main__':
    result = Solution()
    test_case = result.reverseVowels("leetcode")
    print(test_case)