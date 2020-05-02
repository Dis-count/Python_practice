def choose_best_feature_to_split(data_set):
    """
    按照最大信息增益比划分数据
    :param data_set: 样本数据，如： [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    :return:
    """
    num_feature = len(data_set[0]) - 1 # 特征个数，如：不浮出水面是否可以生存	和是否有脚蹼
    base_entropy = calc_shannon_ent(data_set) # 经验熵H(D)
    best_info_gain_ratio = 0.0
    best_feature_idx = -1
    for feature_idx in range(num_feature):
        feature_val_list = [number[feature_idx] for number in data_set]  # 得到某个特征下所有值（某列）
        unique_feature_val_list = set(feature_val_list)  # 获取无重复的属性特征值
        new_entropy = 0
        split_info = 0.0
        for value in unique_feature_val_list:
            sub_data_set = split_data_set(data_set, feature_idx, value)
            prob = len(sub_data_set) / float(len(data_set))  # 即p(t)
            new_entropy += prob * calc_shannon_ent(sub_data_set)  # 对各子集香农熵求和
            split_info += -prob * log(prob, 2)
        info_gain = base_entropy - new_entropy  # 计算信息增益，g(D,A)=H(D)-H(D|A)
        if split_info == 0:  # fix the overflow bug
            continue
        info_gain_ratio = info_gain / split_info
        # 最大信息增益比
        if info_gain_ratio > best_info_gain_ratio:
            best_info_gain_ratio = info_gain_ratio
            best_feature_idx = feature_idx

    return best_feature_idx
