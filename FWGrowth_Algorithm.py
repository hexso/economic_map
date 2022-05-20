'''
데이터들간의 관계를 찾기 위한 알고리즘

'''
import mlxtend
import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import fpgrowth
import time
import pandas as pd
import os

start = time.time() # 시작 시간 저장

def make_data():
    '''
    데이터 형식이 날짜마다 증가한 데이터, 감소한데이터 끼리 묶어서 리스트를 만든다
    그래서 총 리스트를 반환한다.
    :return:
    '''
    file_list = os.listdir('data/')
    file_list_csv = [file for file in file_list if file.endswith(".csv")]
    data = pd.DataFrame()
    for file in file_list_csv:
        source_name = file.split(' ')[0]
        if data.size == 0:
            data = pd.read_csv('data/'+file)
            data.index = data['날짜']
            data = data['변동 %']
            data = data.rename(source_name)
            continue
        new_data = pd.read_csv('data/'+file)
        new_data.index = new_data['날짜']
        new_data = new_data['변동 %']
        new_data = new_data.rename(source_name)
        data = pd.merge(data, new_data, left_index=True, right_index=True)
    data = data.replace("%","",regex=True)
    data = data.astype(float)
    result = []
    for i in range(data.index.size):
        posi = data.iloc[i] >= 0
        nega = data.iloc[i] < 0
        positive_list = data.iloc[i][posi].index.to_list()
        negative_list = data.iloc[i][nega].index.to_list()
        result.append(positive_list)
        result.append(negative_list)
    return result

def get_relation(data):
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    min_support_per = 0.25
    min_trust_per = 0.7
    result = fpgrowth(df,min_support=min_support_per, use_colnames=True)
    result_chart = association_rules(result, metric="confidence", min_threshold=min_trust_per)
    #pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(result_chart)
    print("time: ", time.time() - start) # 현재시각 - 시작시간 = 실행시간

if __name__ == '__main__':
    data = make_data()
    get_relation(data)