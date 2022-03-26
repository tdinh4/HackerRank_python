'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Parameter:
----------
    s: str

Return:
---------
    bool: boolean

Example1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = False
        if s == " ":
            result = True
            return result
        else:
            cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
            n = len(cleaned_s)
            i, j = 0, n - 1
            while (i<n):
                if (cleaned_s[i] == cleaned_s[j]):
                    i += 1
                    j -= 1
                else:
                    result = False
                    return result
            result = True
            return result

if __name__ == '__main__':
    result = Solution()
    test_case = result.isPalindrome("A man, a plan, a canal: Panama")
    print(test_case)