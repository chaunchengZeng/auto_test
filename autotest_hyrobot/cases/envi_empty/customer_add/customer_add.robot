*** Settings ***

Library  customer_add.py   WITH NAME  M

Library  customer_add.C1   WITH NAME  C1



*** Test Cases ***

添加客户API-0151：使用工具发送 添加客户的 API 请求，客户名、电话号码、地址 均符合接口规范
  [Setup]     C1.setup
  [Teardown]  C1.teardown

  C1.teststeps
