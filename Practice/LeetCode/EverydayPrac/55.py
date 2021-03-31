# 173. 二叉搜索树迭代器
#
# 实现一个二叉搜索树迭代器类 BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
#
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。

# 输入
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]

# 输出
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# 方法一：提前保存全部节点  复杂度较大
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()


    def hasNext(self):
        return len(self.queue) > 0


# 时间复杂度：构造函数是 O(N)；调用 next() 方法的时间复杂度是 O(1)。
# 空间复杂度：O(N)，使用了队列保存了所有元素。

# 方法二：迭代时计算 next  节点 // 单调栈

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0

# 时间复杂度：均摊复杂度是 O(1)，调用 next() 方法的时候，如果栈顶元素有右子树，则把所有右边节点及其所有左孩子全部放到了栈中，下次调用 next() 的时候，直接访问栈顶就可以了，均摊之后时间复杂度是 O(1)。
# 空间复杂度：O(h)，h 为数的高度，因为栈中只保留了左节点，栈中元素最多的时候，就是树的高度。
