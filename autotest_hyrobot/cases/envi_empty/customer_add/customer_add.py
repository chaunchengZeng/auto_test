from hyrobot.common import *
from lib.webAPI import api_mgr

"""添加客户的测试"""


class C1(object):
    name = "添加客户API-0151：使用工具发送 添加客户的 API 请求，客户名、电话号码、地址 均符合接口规范"

    def setup(self):
        pass

    def teardown(self):
        api_mgr.customer_del(self.c_id)

    def teststeps(self):
        response = api_mgr.customer_add(name="宋江",
                                        phone_number="12345678", address="山东梁山")

        ret = response.json()
        self.c_id = ret['id']
        INFO(ret)
        CHECK_POINT("判断返回的消息体", ret == {
            "ret": 0,
            "id": self.c_id,
        })
