'''
기본 원자재 같은 data들을 정의하는 곳.
'''
from dataclasses import dataclass
from dataclasses import field


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

#경재요소
Data(name='소득'), Data(name='자산'), Data(name='부동산')

#식료품
Data(name='닭고기'), Data(name='돼지고기'), Data(name='소고기'), Data(name='양고기'), Data(name='오리고기'), Data(name='')

#전자제품
Data(name='반도체'), Data(name=''), Data(name=''), Data(name='')

#농업
Data(name='소득'), Data(name=''), Data(name='')


#

if __name__ == '__main__':
    stock = Data(name='주식')
    pork = Data(name='돼지고기')
    steak = Data(name='소고기')
    print(data_dict)

