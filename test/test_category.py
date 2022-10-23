
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
    Category_main,
    retrieve_category,
    uRl_test_category,
    All_test_data,
    retrieve_all_test_data,
    retrieve_testdata_with_adapter,
    requests_adapter,
    #urllib_adapter
    ## for test
    #retrive_test_category,
)

@pytest.fixture()
def local_baseline_json():
    """Fixture that returns a static baseline."""
    with open("test/resources/api_baseline.json") as f:
        return json.load(f)

@pytest.fixture()
def local_fakeline_json():
    """Fixture that returns a static baseline."""
    with open("test/resources/api_baseline_fake.json") as f:
        return json.load(f)

@pytest.fixture()
def local_promotion_json():
    """Fixture that returns a static baseline."""
    with open("test/resources/api_baseline.json") as f:
        temp = json.load(f)
        return jsonpath.jsonpath(temp, '$..Promotions')


#1st. hardcode for gallery postion in Promotions[1]
@responses.activate
def test_retrieve_Category_using_responses(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK,passthrough=True,)
    category_info = retrieve_category()
    assert category_info == Category_main.from_dict(local_baseline_json)

#2nd way: No matter where is Gallery, we can this to compare the right Description
@responses.activate
def test_retrieve_Promotion_using_responses(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK,passthrough=True)
    #online test data, by using passthrough to trigger real http request
    online_test_data = retrieve_all_test_data()
    assert online_test_data == All_test_data.ds_test_target(local_baseline_json)

#3rd way: using adapter
@responses.activate
def test_retrieve_promotion_using_adapter(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK,passthrough=True)

    online_test_data = retrieve_testdata_with_adapter(adapter=requests_adapter)
    #you can change the adaptar to use another way of request webpage
    #online_test_data = retrieve_testdata_with_adapter(adapter=urllib_adapter)
    assert online_test_data == All_test_data.ds_test_target(local_baseline_json)

#4th way: using VCR.py