"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


"""
Approach 1 - Set
We use a set (charSet) to keep track of unique characters in the current substring.
We maintain two pointers, left and right, to represent the boundaries of the current substring.
The maxLength variable keeps track of the length of the longest substring encountered so far.
We iterate through the string using the right pointer.
If the current character is not in the set (charSet), it means we have a new unique character.
We insert the character into the set and update the maxLength if necessary.
If the character is already present in the set, it indicates a repeating character within the current substring.
In this case, we move the left pointer forward, removing characters from the set until the repeating character is no longer present.
We insert the current character into the set and continue the iteration.
Finally, we return the maxLength as the length of the longest substring without repeating characters.
"""


def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            res = max(res,right-left+1)
        return res
