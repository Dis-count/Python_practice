# 783. Minimum Distance Between BST Nodes
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
#
# Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#
# Example 1:
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
# Example 2:
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# 方法一：数组保存中序遍历结果
# 这个方法是最直观的，也不容易出错的。
#
# 先中序遍历，把结果放在数组中；
# 然后对数组中的相邻元素求差，得到所有差值的最小值。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        self.vals = []
        self.inOrder(root)
        return min([self.vals[i + 1] - self.vals[i] for i in xrange(len(self.vals) - 1)])

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.vals.append(root.val)
        self.inOrder(root.right)

# 时间复杂度：O(N)，因为每个节点只访问了一次；
# 空间复杂度：O(N)，因为需要数组保存二叉树的每个节点值。

# 方法二：只保存上个节点
# 在方法一中，我们保存了整个中序遍历数组，比较浪费空间。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        self.prev = None
        self.minDiff = 10e6
        self.inOrder(root)
        return self.minDiff

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.prev:
            self.minDiff = min(root.val - self.prev.val, self.minDiff)
        self.prev = root
        self.inOrder(root.right)

# 时间复杂度：O(N)，因为每个节点只访问了一次；
# 空间复杂度：O(N)，因为递归用了系统栈。
