# 993. Cousins in Binary Tree
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# Example 1:
#
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Example 2:
#
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
# # Example 3:
#
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

# 深度相同 父节点不同

# 1、 深度优先搜索  栈
# 我们只需要在深度优先搜索的递归函数中增加表示「深度」以及「父节点」的两个参数即可。

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # x 的信息
        x_parent, x_depth, x_found = None, None, False
        # y 的信息
        y_parent, y_depth, y_found = None, None, False

        def dfs(node: TreeNode, depth: int, parent: TreeNode):
            if not node:
                return

            nonlocal x_parent, y_parent, x_depth, y_depth, x_found, y_found

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True

            # 如果两个节点都找到了，就可以提前退出遍历
            # 即使不提前退出，对最坏情况下的时间复杂度也不会有影响
            if x_found and y_found:
                return

            dfs(node.left, depth + 1, node)

            if x_found and y_found:
                return

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent

# 2、 广度优先搜索   队列

# 在广度优先搜索的过程中，每当我们从队首取出一个节点，它就会作为「父节点」，将最多两个子节点放入队尾。因此，除了节点以外，我们只需要在队列中额外存储「深度」的信息即可。

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # x 的信息
        x_parent, x_depth, x_found = None, None, False
        # y 的信息
        y_parent, y_depth, y_found = None, None, False

        # 用来判断是否遍历到 x 或 y 的辅助函数
        def update(node: TreeNode, parent: TreeNode, depth: int):
            if node.val == x:
                nonlocal x_parent, x_depth, x_found
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                nonlocal y_parent, y_depth, y_found
                y_parent, y_depth, y_found = parent, depth, True

        q = collections.deque([(root, 0)])
        update(root, None, 0)

        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
                update(node.left, node, depth + 1)
            if node.right:
                q.append((node.right, depth + 1))
                update(node.right, node, depth + 1)

            if x_found and y_found:
                break

        return x_depth == y_depth and x_parent != y_parent
