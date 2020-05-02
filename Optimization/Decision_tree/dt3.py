# 数据转化
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# import pydotplus
# from sklearn.externals.six import StringIO

if __name__ == '__main__':
    # 加载文件
    with open('lenses.txt', 'r') as fr:
        # 处理文件
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    # 提取每组数据的类别，保存在列表里
    lenses_target = []
    for each in lenses:
        lenses_target.append(each[-1])
    # 特征标签
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    # 保存lenses数据的临时列表
    lenses_list = []
    # 保存lenses数据的字典，用于生成pandas
    lenses_dict = {}
    # 提取信息，生成字典
    for each_label in lensesLabels:
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list = []
        # 打印字典信息
    print(lenses_dict)
    #生成pandas.DataFrame
    lenses_pd = pd.DataFrame(lenses_dict)
    # print(lenses_pd)
    # 生成pandas.DataFrame
    lenses_pd = pd.DataFrame(lenses_dict)
    # 打印pandas.DataFrame
    print(lenses_pd)
    # 创建LabelEncoder()对象，用于序列化
    le = LabelEncoder()
    # 为每一列序列化
    for col in lenses_pd.columns:
        lenses_pd[col] = le.fit_transform(lenses_pd[col])
    print(lenses_pd)
