*** Settings ***

Library  customer_test.py   WITH NAME  M

Library  customer_test.C1   WITH NAME  C1

Library  customer_test.C2   WITH NAME  C2

Library  customer_test.C3   WITH NAME  C3

Library  customer_test.C4   WITH NAME  C4

Library  customer_test.C5   WITH NAME  C5

Library  customer_test.C6   WITH NAME  C6



*** Test Cases ***

列出客户API-0102: 请求消息头中携带登录成功的session id
  [Setup]     C1.setup
  [Teardown]  C1.teardown

  C1.teststeps


列出客户API-0103: pagenum="hello"，pagesize=10，keywords=空字符串
  [Setup]     C2.setup
  [Teardown]  C2.teardown

  C2.teststeps


列出客户API-0104: pagenum=1，pagesize="hello"，keywords=空字符串
  [Setup]     C3.setup
  [Teardown]  C3.teardown

  C3.teststeps


列出客户API-0105: pagenum丢失
  [Setup]     C4.setup
  [Teardown]  C4.teardown

  C4.teststeps


列出客户API-0106: pagesize丢失
  [Setup]     C5.setup
  [Teardown]  C5.teardown

  C5.teststeps


列出客户API-0107: keywords丢失
  [Setup]     C6.setup
  [Teardown]  C6.teardown

  C6.teststeps
