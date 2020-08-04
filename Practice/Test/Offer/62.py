# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）
# 中，按结点数值大小顺序第三小结点的值为4。

# python解法，要注意，返回的是节点，而不是节点的值！！！尼玛，被坑了。

# //思路：二叉搜索树按照中序遍历的顺序打印出来正好就是排序好的顺序。
# //     所以，按照中序遍历顺序找到第k个结点就是结果。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.res=[]
        self.dfs(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None
    def dfs(self,root):
        if not root:return
        self.dfs(root.left)
        self.res.append(root)
        self.dfs(root.right)

a = Solution()

a.KthNode(tree,1)
