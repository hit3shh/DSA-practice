'''
Leetcode problem 560 :

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2
    
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum,count = 0,0
        dict = {0:1}

        for i in range(len(nums)):
            sum += nums[i]

            if dict.get(sum-k) != None :
                count += dict.get(sum-k)    # if sum exists-> count+1
            
            dict[sum] = dict.get(sum,0) + 1    # in dict:  if sum exist-> +1  ... or stores 0 
            
        return count
    
# nums= [1,1,1]  , k=2
# dict= { sum:index   1:0, 2:1, 3:2}   # sum of subaaray[1,1]index[0,1]-> count=1   # another subarray[1,1]index[1,2]-> count of sum2 = 2

