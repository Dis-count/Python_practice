import pickle
"""
函数说明：存储决策树
Parameters：
    inputTree：已经生成的决策树
    filename：决策树的存储文件名
Returns：
    无
Modify：
    2018-03-13

"""
def storeTree(inputTree,filename):
    with open(filename,'wb') as fw:
        pickle.dump(inputTree,fw)

if __name__=='__main__':
    myTree={'有自己的房子':{0:{'有工作':{0:'no',1:'yes'}},1:'yes'}}
    storeTree(myTree,'classifierStorage.txt')
