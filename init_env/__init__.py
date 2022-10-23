
"""
Test Target:
    Name = "Carbon credits"
    CanRelist = true
    The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
"""

import requests
#import json
import jsonpath
from dataclasses import asdict, dataclass
#import urllib.request
from typing import Callable


bAse_url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json"
uRl_test_category = bAse_url + "?catalogue=false"

#1. hardcode for gallery postion to [1]
@dataclass

class Category_main:
    Name: str
    CanRelist: bool
    Name_Promotion: str
    Description: str
    @classmethod
    def from_dict(cls, data: dict) -> "Category_main":
        return cls(
            Name=data["Name"],
            CanRelist=data["CanRelist"],
            Name_Promotion=data["Promotions"][1]['Name'],
            Description=data["Promotions"][1]["Description"],
        )

def find_category_for() -> dict:
    resp = requests.get(uRl_test_category)
    return resp.json()

def retrieve_category() -> Category_main:
    data = find_category_for()
    return Category_main.from_dict(data)

#2. free where for the gallery postion
#a. promotion class, to make the promotion dict
@dataclass
class Promotions_data:
    promotion_name: list
    promotion_description: list
    @classmethod
    def from_dict_loop(cls, data: dict) -> "Promotions_data":
        return cls(
            promotion_name=jsonpath.jsonpath(data,'$.Promotions...Name'),
            promotion_description=jsonpath.jsonpath(data,'$.Promotions...Description'),
        )
#b. test target data format
@dataclass
class All_test_data:
    Name: str
    CanRelist: bool
    gallery_desc: str
    @classmethod
    def ds_test_target(cls, data: dict) -> "All_test_data":
        return cls(
            Name=data["Name"],
            CanRelist=data["CanRelist"],
            gallery_desc=gallery_desc_fun(data),
        )
# Gallery is set as part of test target, if no 'Gallery', test will fail
def gallery_desc_fun(data) -> str:
    tmp_gallery_desc = Promotions_data.from_dict_loop(data)
    dic_test_promotions_data = promotion_dataclass2dic(tmp_gallery_desc)
    return dic_test_promotions_data['Gallery']

def promotion_dataclass2dic(dataclass)->dict:
    temp = asdict(dataclass)
    m_promotion_name = temp['promotion_name']
    m_promotion_description = temp['promotion_description']
    dic_test_promotions_data = dict(zip(m_promotion_name, m_promotion_description))
    return dic_test_promotions_data

#Get the oneline test data
def retrieve_all_test_data() -> All_test_data:
    data = find_category_for()
    return All_test_data.ds_test_target(data)
#--------------------------------------------
#-3rd: use of adapter -
#--------------------------------------------
def requests_adapter(url: str) -> dict:
    """An adapter that encapsulates requests.get"""
    resp = requests.get(url)
    return resp.json()

# #you can chose different adaptar for you request while no changing for other codes
# def urllib_adapter(url: str) -> dict:
#     """An adapter that encapsulates urllib.urlopen"""
#     with urllib.request.urlopen(url) as response:
#         resp = response.read()
#     return json.loads(resp)

def find_testdata_with_adapter(adapter: Callable[[str], dict]) -> dict:
    """Find the online data using an adapter."""
    return adapter(uRl_test_category)

def retrieve_testdata_with_adapter(
    adapter: Callable[[str], dict]
) -> All_test_data:
    """Retrieve online data implementation that uses an adapter."""
    data = find_testdata_with_adapter(adapter=adapter)
    return All_test_data.ds_test_target(data)

# --------------
# for test- mock a joson with error
#---------------
# def fake_baseline_json():
#     """Fixture that returns a static baseline."""
#     with open("test/resources/api_baseline_fake.json") as f:
#         return json.load(f)
#
# def retrive_test_category()-> Category_main:
#     data = fake_baseline_json()
#     return Category_main.from_dict(data)
#---------------