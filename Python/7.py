"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000
"""

class Solution:
    def longestPalindrome(self, s):
        maxLength = 1
        for ind,char in enumerate(s):
            if maxLength >= (len(s)-ind):
                break
            for end in range(len(s),ind+maxLength,-1):
                substr = s[ind:end]
                if maxLength >= len(substr):
                    break
                if self.Palindrome(substr):
                    if len(substr) > maxLength:
                        maxLength = len(substr)
        return maxLength

    def Palindrome(self, s):
        return s == s[::-1]

        


if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    longest = sol.longestPalindrome(s)
    print(longest)
