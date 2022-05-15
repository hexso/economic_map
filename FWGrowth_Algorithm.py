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
import pandas_datareader as pdr

start = time.time() # 시작 시간 저장
data = np.array([
    ['우유','기저귀','쥬스'],
    ['상추','기저귀','맥주'],
    ['우유','양상추','기저귀','맥주'],
    ['양상추','맥주']
])

def get_relation(data):
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    min_support_per = 0.5
    min_trust_per =0.5
    result = fpgrowth(df,min_support=min_support_per, use_colnames=True)
    result_chart = association_rules(result, metric="confidence", min_threshold=min_trust_per)
    #pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(result_chart)
    print("time: ", time.time() - start) # 현재시각 - 시작시간 = 실행시간