# 2215. Find the Difference of Two Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.


## attempt 1
# class Solution(object):
#     def findDifference(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[List[int]]
#         """
#         nums1_new = []
#         nums2_new = []

#         for i in range(len(nums1)):
#             if (nums1[i] not in nums2 and nums1[i] not in  nums1_new):
#                 nums1_new.append(nums1[i])

#         for j in range(len(nums2)):
#             if (nums2[j] not in nums1 and nums2[j] not in nums2_new):
#                 nums2_new.append(nums2[j])

#         return [nums1_new, nums2_new]

## attemp2

# class Solution(object):
#     def findDifference(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[List[int]]
#         """
#         nums1_new = []
#         nums1 = list(set(nums1))
#         nums2 = list(set(nums2))


#         for i in range(len(nums1)):
#             if (nums1[i] not in nums2):
#                 if (nums1[i] not in  nums1_new):
#                     nums1_new.append(nums1[i])
#             else:
#                 nums2.remove(nums1[i])

#         return [nums1_new, nums2]

## attemp 3 - optimal

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1_new = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1 - nums2), list(nums2 - nums1)]