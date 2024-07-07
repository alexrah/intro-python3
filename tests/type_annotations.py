from typing import Literal, Annotated
from annotated_types import Interval, Len
from pydantic import BaseModel
from devtools import debug
from rich import print

tCount = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Inventory(BaseModel):
    count: Annotated[int, Interval(ge=0, le=10)]
    item: Annotated[str, Len(min_length=3)]

    class Config:
        validate_assignment = True
    # count: int


def print_items(count: tCount, obj_type: str, color: str = 'purple') -> None:
    print(f"{count} {obj_type} of color {color} ")


print_items('10', 'phone', 'blue')
print_items(color='red', count=26, obj_type='table')
testPydantic = Inventory(count=9, item='sas')
print(testPydantic)
debug(testPydantic)
testPydantic.count = '123123'

# testPydantic.__setattr__('count', 6)
# debug(testPydantic.model_json_schema())
# debug(testPydantic)


