"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.
You may assume that each input woud have exactly one solution, and you
may not use the same element twice
"""

class Solution:
    def twoSum(self, nums, target):
        mydict = {}
        for ind,num in enumerate(nums):
            if num in mydict:
                return([mydict[num],ind])
            else:
                mydict[target - num] = ind
        return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 17
    solution = Solution()
    sol = solution.twoSum(nums, target)
    print(sol)
