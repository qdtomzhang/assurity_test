
"""
Test Target:
    Name = "Carbon credits"
    CanRelist = true
    The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
"""

import requests
import json
import jsonpath
from dataclasses import asdict, dataclass

bAse_url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json"
uRl_test_category = bAse_url + "?catalogue=false"
#1. hardcode for gallery postion to [1]
@dataclass
class Category_c:
    Name: str
    CanRelist: bool
    Name_Promotion: str
    Description: str
    @classmethod
    def from_dict(cls, data: dict) -> "Category_c":
        return cls(
            Name=data["Name"],
            CanRelist=data["CanRelist"],
            Name_Promotion=data["Promotions"][1]['Name'],
            Description=data["Promotions"][1]["Description"],
        )

def find_category_for() -> dict:
    resp = requests.get(uRl_test_category)
    return resp.json()

def retrieve_category() -> Category_c:
    data = find_category_for()
    return Category_c.from_dict(data)

#2. free where for the gallery postion
#a. promotion class, to make the promotion dict
@dataclass
class Promotions_data:
    promotion_name: list
    promotion_description: list
    @classmethod
    def from_dict_loop(cls, data: dict) -> "Promotions_data":
        return cls(
            promotion_name=jsonpath.jsonpath(data,'$..Name'),
            promotion_description=jsonpath.jsonpath(data,'$..Description'),
        )
#b. test target data format
@dataclass
class All_Promotions_data:
    Name: str
    CanRelist: bool
    gallery_desc: str
    @classmethod
    def ds_test_target(cls, data: dict) -> "All_Promotions_data":
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

# get all promotion data as dict from URL
def find_promotion_for() -> dict:
    resp = requests.get(uRl_test_category)
    temp = resp.json()
    return temp['Promotions']

#get all promation data as dataclasses format
def retrieve_promotion() -> Promotions_data:
    data = find_promotion_for()
    return Promotions_data.from_dict_loop(data)

#to make the promotion dict from dataclass
def retrieve_online_promotion_data() -> dict:
    data = ()
    tmp_Promotions_data = Promotions_data.from_dict_loop(data)
    dic_test_promotions_data = promotion_dataclass2dic(tmp_Promotions_data)
    return dic_test_promotions_data

#Get the oneline test data
def retrieve_all_test_data() -> All_Promotions_data:
    data = find_category_for()
    return All_Promotions_data.ds_test_target(data)
