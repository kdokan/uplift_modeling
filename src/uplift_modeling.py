
#%%
###
# テストデータを作成する
###

import random

def generate_sample_data(num, seed = 1):
    #返却するリストを確保
    is_cv_list = []
    is_treat_list = []
    feature_vector_list = []

    # 乱数を初期化
    random_instance = random.Random(seed)

    # 返す関数の特徴を設定
    feature_num = 8
    base_weight = [0.02, 0.03, 0.05, -0.04, 0.00, 0.00, 0.00, 0.00]
    lift_weight = [0.00, 0.00, 0.00, 0.05, -0.05, 0.00, 0.00, 0.00]

    for i in range(num):
        # 特徴ベクトルを乱数で生成
        feature_vector = [random_instance.random() for n in range(feature_num)]

        # 実験群かどうかを乱数で決定
        is_treat = random_instance.choice((True, False))
        # 内部的なコンバージョンレートを算出
        cv_rate = sum([feature_vector[n] * lift_weight[n] for n in range(feature_num)])

        if is_treat:
            # 実験群であれば、lift_weightを加味する
            cv_rate += sum([feature_vector[n] * lift_weight[n] for n in range(feature_num)])

        # 実際にコンバージョンしたかどうかを決定する
        is_cv = cv_rate > random_instance.random()

        # 生成した値を格納
        is_cv_list.append(is_cv)
        is_treat_list.append(is_treat)
        feature_vector_list.append(feature_vector)

    # 値を返す
    return is_cv_list, is_treat_list, feature_vector_list
generate_sample_data(2)



# %%
