from hyrobot.common import *
from lib.webAPI import api_mgr


class C1(object):
    name = '登陆API-0001: 正确的用户名和登录密码'

    def setup(self):
        INFO('0001初始化')

    def teardown(self):
        INFO('0001介绍')

    def teststeps(self):
        response = api_mgr.mgr_login()
        ret = response.json()
        INFO(ret)
        CHECK_POINT("返回的ret", ret == {"ret": 0})


class C2(object):
    name = '登录API-0002: 正确的用户名，错误的密码'

    def setup(self):
        INFO("0002初始化")

    def teardown(self):
        INFO("0002结束")

    def teststeps(self):
        response = api_mgr.mgr_login(password='88888887')
        ret = response.json()
        INFO(ret)
        CHECK_POINT("返回的ret", ret == {
                                                "ret": 1,
                                                "msg":  "用户名或者密码错误"
                                            })


class C3(object):
    name = '登陆API-0003: 只填写密码'

    def setup(self):
        # self.api_mgr = webAPI.APIMgr()
        pass

    def teardown(self):
        pass

    def teststeps(self):
        response = api_mgr.mgr_login(username='')
        ret = response.json()
        INFO(ret)
        CHECK_POINT("返回的ret", ret == {
            "ret": 1,
            "msg": "用户名或者密码错误"
        })


class C4(object):
    name = '登陆API-0004: 只填写用户名'

    def setup(self):
        # self.api_mgr = webAPI.APIMgr()
        pass

    def teardown(self):
        pass

    def teststeps(self):
        response = api_mgr.mgr_login(password='')
        ret = response.json()
        INFO(ret)
        CHECK_POINT("返回的ret", ret == {
            "ret": 1,
            "msg": "用户名或者密码错误"
        })

