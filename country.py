from dataclasses import dataclass
from dataclasses import field


auto_id = 50000
country_dict = {}


def get_id():
    global auto_id
    auto_id += 1
    return auto_id\


@dataclass
class Country:
    id: int = 0
    name: str = ''
    economic: int = 100
    export_item: dict = field(default_factory=dict)
    import_item: dict = field(default_factory=dict)

    def __post_init__(self):
        self.id = get_id()
        country_dict[self.name] = self

    def __hash__(self):
        return self.id

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

#각 나라별로 수출,수입품목 입력
#품목:품목이 세계시장에서 차지하는 비율
Country(name='사우디아라비아', export_item={'원유':20,'천연가스':3}, import_item={})
Country(name='러시아', export_item={'원유':11,'천연가스':17}, import_item={})
Country(name='이라크', export_item={'원유':7}, import_item={})
Country(name='캐나다', export_item={'원유':6,'천연가스':4}, import_item={})
Country(name='아랍에미리트', export_item={'원유':6}, import_item={})
Country(name='쿠웨이트', export_item={'원유':5}, import_item={})
Country(name='이란', export_item={'원유':4,'천연가스':6}, import_item={})
Country(name='나이지리아', export_item={'원유':4}, import_item={})
Country(name='앙골라', export_item={'원유':4}, import_item={})
Country(name='노르웨이', export_item={'원유':3,'천연가스':3}, import_item={})

Country(name='미국',export_item={'천연가스':23}, import_item={})
Country(name='중국',export_item={'천연가스':5}, import_item={})
Country(name='카타르',export_item={'천연가스':5}, import_item={})
Country(name='오스트레일리아',export_item={'천연가스':4}, import_item={})
Country(name='알제리',export_item={'천연가스':2}, import_item={})
Country(name='말레이시아',export_item={'천연가스':2}, import_item={})
Country(name='인도네시아',export_item={'천연가스':2}, import_item={})
