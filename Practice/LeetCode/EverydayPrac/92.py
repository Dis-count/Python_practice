# 897. Increasing Order Search Tree
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
#
# Example 1:
#
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
# Example 2:
#
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# 遇到二叉搜索树，立刻想到这句话：「二叉搜索树（BST）的中序遍历是有序的」。这是解决所有二叉搜索树问题的关键。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：数组保存中序遍历结果

# 这个方法是最直观的，也不容易出错的。

# 先中序遍历，把结果放在数组中；
# 然后修改数组中每个节点的左右指针：把节点的左指针设置为 null，把节点的右指针设置为数组的下一个节点。

class Solution(object):
    def increasingBST(self, root):
        self.res = []
        self.inOrder(root)
        if not self.res:
            return
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)

# 时间复杂度：O(N)，因为每个节点只访问了一次；
# 空间复杂度：O(N)，因为需要数组保存二叉树的每个节点值。

# 方法二：只保存上个节点


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(-1)
        self.prev = dummy
        self.inOrder(root)
        return dummy.right

    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        root.left = None
        self.prev.right = root
        self.prev = root
        self.inOrder(root.right)


# 时间复杂度：O(N)，因为每个节点只访问了一次；
# 空间复杂度：O(N)，因为递归用了系统栈。
