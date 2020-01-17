from hyrobot.common import *
from lib.webAPI import api_mgr

"""10个客户的初始环境：测试列出客户"""


class C1(object):
    name = '列出客户API-0108: pagenum=1，pagesize=10，keywords=空字符串'

    def setup(self):
        INFO("0108初始化")

    def teardown(self):
        INFO("0108结束")

    def teststeps(self):
        response = api_mgr.customer_list(pagesize=10, pagenumber=1)
        customer_list = api_mgr.customer_list().json()["retlist"]
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret == {
            "ret": 0,
            "retlist": customer_list,
            "total": 10
        })


class C2(object):
    name = '列出客户API-0109: pagenum=2，pagesize=10，keywords=空字符串'

    def setup(self):
        INFO("0109初始化")

    def teardown(self):
        INFO("0109结束")

    def teststeps(self):

        response = api_mgr.customer_list(pagesize=10, pagenumber=2)
        # customer_list = api_mgr.customer_list().json()["retlist"]
        ret = response.json()
        # INFO(ret)
        CHECK_POINT("判断返回的消息体", ret == {
            "ret": 0,
            "retlist": [],
            "total": 0

        })


class C3(object):
    name = '列出客户API-0110: pagenum=3，pagesize=10，keywords=空字符串'

    def setup(self):
        INFO("0110初始化")

    def teardown(self):
        INFO("0110结束")

    def teststeps(self):
        response = api_mgr.customer_list(pagesize=10, pagenumber=3)
        # customer_list = api_mgr.customer_list().json()["retlist"]
        ret = response.json()
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret == {
            "ret": 0,
            "retlist": [],
            "total": 0
        })


class C4(object):
    name = '列出客户API-0111: pagenum=3，pagesize=5，keywords=空字符串'

    def setup(self):
        pass

    def teardown(self):
        pass

    def teststeps(self):
        STEP(3, "测试")
        response = api_mgr.customer_list(pagesize=5, pagenumber=3)
        # customer_list = api_mgr.customer_list().json()["retlist"]
        ret = response.json()
        INFO(ret)
        # INFO(customer_list)
        CHECK_POINT("判断返回的消息体", ret == {
            "ret": 0,
            "retlist": [],
            "total": 0
        })