'''
모든 요소들의 관계에 대한 정의는 이곳에 정의한다.
각각의 요소들의 정의는 각각의 .py파일에 한다.
'''
import datas as da
import stocks as st
from queue import Queue

total_dict = {}
total_dict.update(da.data_dict)
total_dict.update(st.stock_dict)


def add_relation(parent: str, parent_attr: str, child: str, child_attr: str, value):
    '''
    :param parent: 영향을 받는 Data의 name
    :param parent_attr: 영향을 받는 Data의 속성
    :param child: 영향을 주는 Data의 name
    :param child_attr: 영향을 주는 Data의 속성
    :param value: 얼마만큼의 영향을 주는지(0~1) 소수점 단위
    :return: none
    :after: 결국 effecting에는 [영향을 끼치는 data name, 해당 속성, value] 가 추가된다.
    '''
    effecting = list()
    effecting.append(parent)
    effecting.append(parent_attr)
    effecting.append(value)
    total_dict[child].effecting[child_attr].append(effecting)
    effected = list()
    effected.append(child)
    effected.append(child_attr)
    effected.append(value)
    total_dict[parent].effected[parent_attr].append(effected)

def change_attr(name, attr, change, depth=99999999):
    '''
    :param name: 수정할 data의 name
    :param attr: 수정할 data의 속성
    :param change: 값 (0~1)
    :param depth: 몇단계 parent까치 영향을 끼칠건지
    :return:
    '''
    data = total_dict[name]
    if attr == 'demand':
        data.demand *= change
    elif attr == 'supply':
        data.supply *= change
    elif attr == 'value':
        data.value *= change

    changed_id_list = list()
    changed_id_list.append(data.id)
    q = Queue()

    for selected_data in total_dict[name].effecting[attr]:
        li = selected_data.copy()
        li.append(depth)
        q.put(li)

    while not q.empty():
        d = q.get()# [0]: parent name, [1]: 바꾸는 속성, [2]: 바뀌는 변화율, [3]:depth
        if total_dict[d[0]].id in changed_id_list:
            continue
        data = total_dict[d[0]]
        changed_id_list.append(data.id)
        if attr == 'demand':
            data.demand *= change
        elif attr == 'supply':
            data.supply *= change
        elif attr == 'value':
            data.value *= change
        depth = d[3] - 1
        if depth > 0:
            for selected_data in total_dict[name].effecting[attr]:
                li = selected_data.copy()
                li[2] = li[2] * change
                li.append(depth)
                q.put(selected_data)


if __name__ == '__main__':
    print(total_dict)
    add_relation('닭고기', 'value', '돼지고기', 'demand', 0.2)
    add_relation('돼지고기', 'value', '소고기', 'demand', 0.2)
    add_relation('삼성전자', 'value', '반도체', 'value', 1)
    print(total_dict)
    change_attr('돼지고기', 'demand', 0.5)
    change_attr('반도체', 'value', 0.5)
    print(total_dict['삼성전자'])