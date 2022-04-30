'''
주식 리스트들에 대한 dataclass
data와 달리 속성은 주식가격, 주식의 종류(반도체, 바이오와 같은), 영향을 받는 data들을 넣는다.
'''
from dataclasses import dataclass
from dataclasses import field


auto_id = 10000
stock_dict = {}


def get_id():
    global auto_id
    auto_id += 1
    return auto_id


@dataclass
class Stock:
    id: int = 0
    name: str = ''
    value: float = 1
    theme: str = ''
    effected: dict = field(default_factory=dict)

    def __post_init__(self):
        self.id = get_id()
        self.effected['value'] = []
        stock_dict[self.name] = self

    def __hash__(self):
        return self.id

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


Stock(name='삼성전자',theme='반도체')

