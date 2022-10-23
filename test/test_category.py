
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
import vcr

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

# @pytest.fixture()
# def local_promotion_json():
#     """Fixture that returns a static baseline."""
#     with open("test/resources/api_baseline.json") as f:
#         temp = json.load(f)
#         return jsonpath.jsonpath(temp, '$..Promotions')


#No.1: hardcode for gallery postion in Promotions[1]
@responses.activate
def test_retrieve_Category_using_responses(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK,passthrough=True,)
    category_info = retrieve_category()
    assert category_info == Category_main.from_dict(local_baseline_json)

#No.2: No matter where is Gallery, we can this to compare the right Description
@responses.activate
def test_retrieve_Promotion_using_responses(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK,passthrough=True)
    #online test data, by using passthrough to trigger real http request
    online_test_data = retrieve_all_test_data()
    assert online_test_data == All_test_data.ds_test_target(local_baseline_json)

#No.3: using adapter
# You can choose to use responses to initiate the test, also you can trigger it by test_ only
@responses.activate
def test_retrieve_promotion_using_adapter(local_baseline_json):
    responses.add(responses.GET, uRl_test_category, json=local_baseline_json, status=HTTPStatus.OK,passthrough=True)

    online_test_data = retrieve_testdata_with_adapter(adapter=requests_adapter)
    #you can change adaptar to use another way to request webpage - e.g.:by urllib
    #online_test_data = retrieve_testdata_with_adapter(adapter=urllib_adapter)
    assert online_test_data == All_test_data.ds_test_target(local_baseline_json)

#-No.4: use of vcr.py
#On Oct.23, the test server was abnormal, so I think we should have a way to test offline, then I found vcr.py
#You can run the test online for the first time, then a ***_vcr file will be created.
#Then you can run the test without the network. The others tests will fail, but this one will still success
#If the online API is changed, you need to delete ***_vcr and re-generate the files again.

@vcr.use_cassette()
def test_retrieve_test_using_vcr(local_baseline_json):
    category_info = retrieve_category()
    assert category_info == Category_main.from_dict(local_baseline_json)


