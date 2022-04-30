from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from queue import Queue


auto_id = 0
data_dict = {}


def get_id():
    global auto_id
    auto_id += 1
    return auto_id


@dataclass
class Data:
    id: int = 0
    name: str = ''
    demand: int = 100
    supply: int = 100
    value: float = 1
    effecting: dict = field(default_factory=dict)
    effected: dict = field(default_factory=dict)

    def __post_init__(self):
        self.value = self.demand/self.supply
        self.id = get_id()
        self.effecting['value'] = []
        self.effecting['supply'] = []
        self.effecting['demand'] = []
        self.effected['supply'] = []
        self.effected['demand'] = []
        self.effected['value'] = []
        data_dict[self.name] = self

    def __hash__(self):
        return self.id

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == 'demand' or key == 'supply':
            super().__setattr__('value', self.demand/self.supply)


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
    data_dict[child].effecting[child_attr].append(effecting)
    effected = list()
    effected.append(child)
    effected.append(child_attr)
    effected.append(value)
    data_dict[parent].effected[parent_attr].append(effected)

def change_attr(name, attr, change, depth=99999999):
    '''
    :param name: 수정할 data의 name
    :param attr: 수정할 data의 속성
    :param change: 값 (0~1)
    :param depth: 몇단계 parent까치 영향을 끼칠건지
    :return:
    '''
    data = data_dict[name]
    if attr == 'demand':
        data.demand *= change
    elif attr == 'supply':
        data.supply *= change
    elif attr == 'value':
        data.value *= change

    changed_id_list = list()
    changed_id_list.append(data.id)
    q = Queue()

    for selected_data in data_dict[name].effecting[attr]:
        li = selected_data.copy()
        li.append(depth)
        q.put(li)

    while not q.empty():
        d = q.get()# [0]: parent name, [1]: 바꾸는 속성, [2]: 바뀌는 변화율, [3]:depth
        if data_dict[d[0]].id in changed_id_list:
            continue
        data = data_dict[d[0]]
        changed_id_list.append(data.id)
        if attr == 'demand':
            data.demand *= change
        elif attr == 'supply':
            data.supply *= change
        elif attr == 'value':
            data.value *= change
        depth = d[3] - 1
        if depth > 0:
            for selected_data in data_dict[name].effecting[attr]:
                li = selected_data.copy()
                li[2] = li[2] * change
                li.append(depth)
                q.put(selected_data)





if __name__ == '__main__':
    stock = Data(name='주식')
    pork = Data(name='돼지고기')
    steak = Data(name='소고기')
    add_relation('주식', 'value', '돼지고기', 'demand', 0.2)
    add_relation('돼지고기', 'value', '소고기', 'demand', 0.2)
    print(stock)
    stock.supply = 200
    print(stock)
    print(data_dict)
    change_attr('돼지고기', 'demand', 0.5)
    print(data_dict)

