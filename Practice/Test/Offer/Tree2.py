class Node:
    def __init__(self,value = None,left = None,right = None):
         self.value = value
         self.left = left    #左子树
         self.right = right  #右子树
def preTraverse(root):
    '''
    前序遍历
    '''
    if root==None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root):
    '''
    中序遍历
    '''
    if root==None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)

def afterTraverse(root):
    '''
    后序遍历
    '''
    if root==None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

if __name__=='__main__':
    root = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print('前序遍历：')
    preTraverse(root)
    print('\n')
    print('中序遍历：')
    midTraverse(root)
    print('\n')
    print('后序遍历：')
    afterTraverse(root)
    print('\n')
