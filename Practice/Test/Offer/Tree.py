# 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
class Node(object):
    """结点类"""
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

#树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class BinaryTree(object):
    """二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """
        广度优先遍历方式添加结点
        :param item:
        :return:
        """
        if self.root is None:
            self.root = Node(item)
        else:
            queue = []
            queue.append(self.root)

            while len(queue) > 0:
                node = queue.pop(0)
                if not node.lchild:
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(node.rchild)

    def breadh_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue)>0:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)


#先序遍历 在先序遍历中，我们先访问根节点，然后递归使用先序遍历访问左子树，再递归使用先序遍历访问右子树
# 根节点->左子树->右子树
    def preorder_travel(self, root):
    # 先序 根 左 右
        if root:
            print(root.item, end=" ")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)


#中序遍历 在中序遍历中，我们递归使用中序遍历访问左子树，然后访问根节点，最后再递归使用中序遍历访问右子树
# 左子树->根节点->右子树
    def inorder_travel(self, root):
    # 中序 左 根 右
        if root:
            self.inorder_travel(root.lchild)
            print(root.item, end=" ")
            self.inorder_travel(root.rchild)


#后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
# 左子树->右子树->根节点
    def postorder_travel(self, root):
    # 后序 左 右 根
        if root:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end=" ")


if  __name__=="__main__":
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadh_travel()
    print("")
    tree.preorder_travel(tree.root)
    print("")
    tree.inorder_travel(tree.root)
    print("")
    tree.postorder_travel(tree.root)
    print("")
