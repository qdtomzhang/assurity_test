
"""
Test for:
    Name = "Carbon credits"
    CanRelist = true
    The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
"""

import json
import pytest
import responses
from http import HTTPStatus
import jsonpath


from init_env import (
    Category_c,
    retrieve_category,
    uRl_test_category,
    All_Promotions_data,
    retrieve_all_test_data

)

@pytest.fixture()
def local_baseline_json():
    """Fixture that returns a static baseline."""
    with open("test/resources/api_baseline.json") as f:
        return json.load(f)

@pytest.fixture()
def local_promotion_json():
    """Fixture that returns a static baseline."""
    with open("test/resources/api_baseline.json") as f:
        temp = json.load(f)
        return jsonpath.jsonpath(temp, '$..Promotions')


#1. hardcode for gallery postion to [1]
@responses.activate
def test_retrieve_Category_using_responses(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK)
    category_info = retrieve_category()
    assert category_info == Category_c.from_dict(local_baseline_json)


#2nd way: No matter where is Gallery, we can this to compare the right Description
@responses.activate
def test_retrieve_Promotion_using_responses(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK)

    #online test data
    online_test_data = retrieve_all_test_data()
    # compare with offine test data
    assert online_test_data == All_Promotions_data.ds_test_target(local_baseline_json)

