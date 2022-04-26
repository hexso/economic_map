from dataclasses import dataclass
from dataclasses import field
auto_id = 0


def get_id():
    global auto_id
    auto_id += 1
    return auto_id


@dataclass
class Data:
    id: int
    name: str
    value: int
    effecting_data: dict = field(default_factory=dict)
    effected_data: dict = field(default_factory=dict)

    def __hash__(self):
        return self.id

def add_relation(parent: Data, child: Data, value):
    '''
    :param parent: 영향을 받는 Data class
    :param child: 영향을 주는 Data class
    :param value: 얼마만큼의 영향을 주는지
    :return: none
    '''

    parent.effected_data[child] = value
    child.effecting_data[parent] = value


stock = Data(id=get_id(), name='주식', value=1)
pig = Data(id=get_id(), name='돼지', value=1)
add_relation(stock, pig, 1)
