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
        self.value = self.demand/self.supply
        self.id = get_id()
        self.effecting['value'] = []
        self.effecting['supply'] = []
        self.effecting['demand'] = []
        self.effected['supply'] = []
        self.effected['demand'] = []
        self.effected['value'] = []
        country_dict[self.name] = self

    def __hash__(self):
        return self.id

    def __setattr__(self, key, value):
        super().__setattr__(key, value)