'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Parameter:
----------
    s: str
    t: str
Return:
---------
    step: int

Example1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Time: O(n)
'''
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt, step = Counter(s), 0
        for i in t:
            if cnt[i] > 0:
                cnt[i] -= 1
            else:
                step += 1
        return step

if __name__ == '__main__':
    result = Solution()
    test_case = result.minSteps("bab", "aba")
    print(test_case)