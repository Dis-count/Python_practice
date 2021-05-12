# 872. Leaf-Similar Trees
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
# Example 1:
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
# Example 2:
#
# Input: root1 = [1], root2 = [1]
# Output: true
#
# Example 3:
#
# Input: root1 = [1], root2 = [2]
# Output: false
#
# Example 4:
#
# Input: root1 = [1,2], root2 = [2,2]
# Output: true
#
# Example 5:
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)

        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        return seq1 == seq2

# 复杂度分析
# 时间复杂度：O(n_1 + n_2)，其中 n1 和 n2 分别是两棵树的节点个数。
# 空间复杂度：O(n_1 + n_2)。空间复杂度主要取决于存储「叶值序列」的空间以及深度优先搜索的过程中需要使用的栈空间。
