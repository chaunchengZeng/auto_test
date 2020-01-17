from hyrobot.common import *
from lib.webAPI import api_mgr

"""初始化文件：初始化环境为没有客户没有药品没有订单"""


def suite_setup():
    INFO("__st__初始化")
    api_mgr.mgr_login()
    INFO('删除订单，客户和药品')
    api_mgr.order_del_all()
    api_mgr.customer_del_all()
    api_mgr.medicine_del_all()


def suite_teardown():
    INFO('__st__结束')
