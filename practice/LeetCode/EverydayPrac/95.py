# 938. Range Sum of BST
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
#
# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
#
# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23

#  递归
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        res = 0
        if not root:
            return res
        res += self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            res += root.val
        res += self.rangeSumBST(root.right, low, high)
        return res

#  剪枝
# 上面的代码中是题目输入的是普通二叉树来进行计算的，其实题目给出的是个二叉搜索树，所以可以根据其性质进行剪枝。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        res = 0
        if not root:
            return res
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if low <= root.val <= high:
            res += root.val
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        return res

# 时间复杂度：O(N)，因为每个节点都要遍历一次；
# 空间复杂度：O(N)，因为递归需要消耗系统栈。
