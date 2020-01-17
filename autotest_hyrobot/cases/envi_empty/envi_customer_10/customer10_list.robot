*** Settings ***

Library  customer10_list.py   WITH NAME  M

Library  customer10_list.C1   WITH NAME  C1

Library  customer10_list.C2   WITH NAME  C2

Library  customer10_list.C3   WITH NAME  C3

Library  customer10_list.C4   WITH NAME  C4



*** Test Cases ***

列出客户API-0108: pagenum=1，pagesize=10，keywords=空字符串
  [Setup]     C1.setup
  [Teardown]  C1.teardown

  C1.teststeps


列出客户API-0109: pagenum=2，pagesize=10，keywords=空字符串
  [Setup]     C2.setup
  [Teardown]  C2.teardown

  C2.teststeps


列出客户API-0110: pagenum=3，pagesize=10，keywords=空字符串
  [Setup]     C3.setup
  [Teardown]  C3.teardown

  C3.teststeps


列出客户API-0111: pagenum=3，pagesize=5，keywords=空字符串
  [Setup]     C4.setup
  [Teardown]  C4.teardown

  C4.teststeps
