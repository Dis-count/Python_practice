# 363. Max Sum of Rectangle No Larger Than K
# Given an (m x n matrix) matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
#
# It is guaranteed that there will be a rectangle with a sum no larger than k.
#
# Example 1:
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
#
# Example 2:
#
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3

# 转化为「在一维数组中，求解和不超过 K 的最大连续子数组之和」
