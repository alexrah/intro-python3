import csv
from dataclasses import dataclass
from typing import TypedDict, Iterable, get_type_hints
from polars import read_csv
import polars as pl
import sys
import pandas as pd


class Ads(TypedDict):
    order: str
    line_item: str
    order_ID: str
    line_item_ID: str
    line_item_start_time: str
    line_item_end_time: str
    ad_unit_targeting: str
    custom_targeting: str
    targeted_sizes: str


ads_df = read_csv('../data/ads.csv', has_header=True, new_columns=[column for column in get_type_hints(Ads).keys() if not column.startswith('_')])
print(ads_df.schema)
print(ads_df.filter(pl.col('order').str.starts_with('Fed')))
print(ads_df.get_column('order'))


ads_csv: Iterable[Ads] = ads_df.to_dicts()
# print(ads_csv['order'])
for row in ads_csv:
    print(row['order'])


test_df = pl.DataFrame({
    "foo": 'bar'
})

print(test_df['foo'])

test_pd = pd.DataFrame({
    "foo": ["bar"]
})

print(test_pd.foo)

ads_df_typed = pl.LazyFrame(ads_df, schema=get_type_hints(Ads))


with open('../data/ads.csv', 'r') as ads_file:
    ads_list = list(csv.reader(ads_file))
    # print(ads_list[0])
    for row in ads_list:
        print(row)
