import pickle

"""
函数说明:读取决策树

Parameters:
    filename：决策树的存储文件名
Returns:
    pickle.load(fr)：决策树字典
Modify:
    2018-03-13
"""
def grabTree(filename):
    fr = open(filename, 'rb')
    return pickle.load(fr)

if __name__ == '__main__':
    myTree = grabTree('classifierStorage.txt')
    print(myTree)
