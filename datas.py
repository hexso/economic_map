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


#경제요소
Data(name='소득'), Data(name='자산'), Data(name='부동산'), Data(name='한국금리'), Data(name='미국금리'), Data(name='한국채권'), Data(name='미국채권')
Data(name='달러'), Data(name='엔화'), Data(name='원화')

#식료품
Data(name='닭고기'), Data(name='돼지고기'), Data(name='소고기'), Data(name='양고기'), Data(name='오리고기'), Data(name='물고기')
Data(name='양파'), Data(name='빵'), Data(name='파'), Data(name='술'), Data(name='버터')
Data(name='아이스크림'), Data(name='물')

#전자제품
Data(name='반도체'), Data(name='2차전지'), Data(name='스마트폰'), Data(name='노트북'), Data(name='냉장고'), Data(name='TV')


#농업
Data(name='옥수수'), Data(name='대두'), Data(name='밀'), Data(name='커피'), Data(name='콩')
Data(name='쌀'), Data(name='설탕'), Data(name='소금')

#금속
Data(name='니켈'), Data(name='금'), Data(name='은'), Data(name='구리'), Data(name='철강')
Data(name='플라스틱')

#자원
Data(name='원유'), Data(name='천연가스'), Data(name='신재생에너지')
Data(name='비료'), Data(name='사료'), Data(name='전기')

#생활용품
Data(name='의류'), Data(name='화장품'), Data(name='가구'), Data(name='샴푸'), Data(name='담배')
Data(name='책'), Data(name='안경')

#활동
Data(name='여행')

#완제품
Data(name='자동차'), Data(name='타이어')


if __name__ == '__main__':
    stock = Data(name='주식')
    pork = Data(name='돼지고기')
    steak = Data(name='소고기')
    print(data_dict)

