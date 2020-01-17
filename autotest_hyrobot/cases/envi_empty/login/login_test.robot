*** Settings ***

Library  login_test.py   WITH NAME  M

Library  login_test.C1   WITH NAME  C1

Library  login_test.C2   WITH NAME  C2

Library  login_test.C3   WITH NAME  C3

Library  login_test.C4   WITH NAME  C4



*** Test Cases ***

登陆API-0001: 正确的用户名和登录密码
  [Setup]     C1.setup
  [Teardown]  C1.teardown

  C1.teststeps


登录API-0002: 正确的用户名，错误的密码
  [Setup]     C2.setup
  [Teardown]  C2.teardown

  C2.teststeps


登陆API-0003: 只填写密码
  [Setup]     C3.setup
  [Teardown]  C3.teardown

  C3.teststeps


登陆API-0004: 只填写用户名
  [Setup]     C4.setup
  [Teardown]  C4.teardown

  C4.teststeps
