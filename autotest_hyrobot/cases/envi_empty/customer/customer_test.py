from hyrobot.common import *
from lib.webAPI import api_mgr

"""以下为列出客户的测试"""


class C1(object):
    name = '列出客户API-0102: 请求消息头中携带登录成功的session id'

    def setup(self):
        INFO("0102初始化")

    def teardown(self):
        INFO("0102结束")

    def teststeps(self):

        response = api_mgr.customer_list()
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret == {
                                        "ret": 0,
                                        "retlist": [],
                                        'total': 0
                                        })


class C2(object):
    name = '列出客户API-0103: pagenum="hello"，pagesize=10，keywords=空字符串'

    def setup(self):
        INFO("0103初始化")

    def teardown(self):
        INFO("0103结束")

    def teststeps(self):

        response = api_mgr.customer_list(pagesize=10, pagenumber='hello')
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret["ret"] == 2)


class C3(object):
    name = '列出客户API-0104: pagenum=1，pagesize="hello"，keywords=空字符串'

    def setup(self):
        INFO("0104初始化")

    def teardown(self):
        INFO("0104结束")

    def teststeps(self):
        response = api_mgr.customer_list(pagesize="hello", pagenumber=1)
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret["ret"] == 2)


class C4(object):
    name = '列出客户API-0105: pagenum丢失'

    def setup(self):
        INFO("0105初始化")

    def teardown(self):
        INFO("0105结束")

    def teststeps(self):
        response = api_mgr.customer_list(pagenumber=None)
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret["ret"] == 2)


class C5(object):
    name = '列出客户API-0106: pagesize丢失'

    def setup(self):
        INFO("0106初始化")

    def teardown(self):
        INFO("0106结束")

    def teststeps(self):
        response = api_mgr.customer_list(pagesize=None)
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret["ret"] == 2)


class C6(object):
    name = '列出客户API-0107: keywords丢失'

    def setup(self):
        INFO("0107初始化")

    def teardown(self):
        INFO("0107结束")

    def teststeps(self):
        response = api_mgr.customer_list(keywords=None)
        ret = response.json()
        INFO(ret)
        CHECK_POINT("返回的消息体", ret == {
            "ret": 0,
            "retlist": [],
            'total': 0,
        })