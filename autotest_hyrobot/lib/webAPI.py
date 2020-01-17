# coding: utf-8
# Author: zcc

import requests

"""此文件为方法的封装"""


def print_response(response):
    """打印响应"""
    print('\n\n------HTTP response * begin --------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print("")

    print(response.content.decode('utf8'))
    print('-------- HTTP response * end -------\n\n')


class APIMgr(object):
    """方法类的封装"""

    def __init__(self):
        self.s = requests.Session()

    def mgr_login(self, username='byhy', password='88888888',
                  use_proxy=False, username_2=False, password_2=False):
        print("管理员登陆")

        if use_proxy:
            self.s.proxies.update({'http': 'http://127.0.0.1:8888'})

        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                               data={
                                   "username": username,
                                   "password": password,
                               }
                               )

        print_response(response)
        return response

    def customer_list(self, pagesize=10, pagenumber=1, keywords=''):
        # 默认列出第一页的前10个顾客
        print('列出客户')
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
                              params={
                                  'action': 'list_customer',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        print_response(response)
        return response

    def customer_add(self, name, phone_number, address):
        print('添加客户')
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
                               json={
                                   "action": "add_customer",
                                   "data": {
                                       "name": name,
                                       "phonenumber": phone_number,
                                       "address": address
                                   }
                               })

        print_response(response)
        return response

    def customer_add2(self, data):
        print('添加客户2:参数自定义添加')
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
                               json={
                                   "action": "add_customer",
                                   "data": data
                               })

        print_response(response)
        return response

    def customer_del(self, customer_id):
        print('删除指定id客户')
        response = self.s.delete('http://127.0.0.1/api/mgr/customers',
                                 json={
                                     "action": "del_customer",
                                     "id": customer_id
                                 })

        print_response(response)
        return response

    def customer_del_all(self):
        print('删除所有顾客')
        response = self.customer_list(100, 1)
        lis = response.json()['retlist']

        for one in lis:
            self.customer_del(one['id'])

    # 药品操作
    def medicine_list(self, pagesize=10, pagenumber=1, keywords=''):
        # 默认列出第一页的前10种药品
        print('列出药品')
        response = self.s.get("http://127.0.0.1/api/mgr/medicines",
                              params={
                                  'action': 'list_medicine',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        print_response(response)
        return response

    def medicine_del(self, medicine_id):
        print('删除指定id药品')
        response = self.s.delete('http://127.0.0.1/api/mgr/medicine',
                                 json={
                                     "action": "del_medicine",
                                     "id": medicine_id
                                 })

        print_response(response)
        return response

    def medicine_del_all(self):
        print('删除所有药品')
        response = self.medicine_list(100, 1)
        lis = response.json()['retlist']

        for one in lis:
            self.medicine_del(one['id'])

    # 订单操作
    def order_list(self, pagesize=10, pagenumber=1, keywords=''):
        # 默认列出第一页的前10张订单
        print("列出所有订单")
        response = self.s.get("http://127.0.0.1/api/mgr/orders",
                              params={
                                  "action": "list_order",
                                  "pagesize": pagesize,
                                  "pagenum": pagenumber,
                                  "keywords": keywords
                              }
                              )
        print_response(response)
        return response

    def order_del(self, order_id):
        print('删除指定id订单')
        response = self.s.delete("http://127.0.0.1/api/mgr/orders",
                                 json={
                                     "action": "delete_order",
                                     "id": order_id
                                 })

        print_response(response)
        return response

    def order_del_all(self):
        print("删除所有订单")
        response = self.order_list(100, 1)

        lis = response.json()["retlist"]
        for one in lis:
            self.order_del(one["id"])


api_mgr = APIMgr()
