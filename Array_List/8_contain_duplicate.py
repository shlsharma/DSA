'''
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Hint: Use sets
'''
def contain_duplicate(lst):
    return False if len(lst) == len(set(lst)) else True

print(contain_duplicate([1,2,3,1]))

# Time and Space complexity - o(n)