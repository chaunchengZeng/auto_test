from hyrobot.common import *
from lib.webAPI import api_mgr

""""创建环境：10个顾客"""

suite_data_customer_id = []


def suite_setup():
    global suite_data_customer_id
    INFO('添加10个客户')

    for i in range(10):
        r = api_mgr.customer_add(
            f'武汉市桥西医院_{i + 1}',
            f'100000000{i + 1:02d}',
            f"武汉市桥西医院北路_{i + 1}")

        suite_data_customer_id.append(r.json()['id'])


def suite_teardown():
    INFO('删除创建的10个客户')
    global suite_data_customer_id

    for cid in suite_data_customer_id:
        api_mgr.customer_del(cid)
