import re

import jsonpath
import pytest
import requests


class TestApi:

    def test_01_api(self):
        res = requests.get(url="https://b52.xiaoluyy.com/patientApi/common/quick/entry?os=ios&osVersion=17.4&appVersion=8.0.44&deviceModel=IPHONE&specificModel=iPhone%2013%20Pro%20Max%3CiPhone14,3%3E&channel=3&version=3.8.2&bigdataActId=&bigDataEnterType=0&pver=3.8.2")
        print(res.text)
        # 正则表达式提取
        result = re.search('"functionName":"(.*?)"', res.text)
        print(result.group(1))

    def test_02_api(self):
        res = requests.get(url="https://b52.xiaoluyy.com/patientApi/common/quick/entry?os=ios&osVersion=17.4&appVersion=8.0.44&deviceModel=IPHONE&specificModel=iPhone%2013%20Pro%20Max%3CiPhone14,3%3E&channel=3&version=3.8.2&bigdataActId=&bigDataEnterType=0&pver=3.8.2")
        print(res.text)
        # 通过jsonpath取值
        value = jsonpath.jsonpath(res.json(), "$..functionName")
        print(value)


if __name__ == '__main__':
    pytest.main()