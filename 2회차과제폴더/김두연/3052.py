# -*- coding: utf-8 -*-
"""3052.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pWhO3n-bSR61vlY9-NAESzVBrX1BAbbx
"""

li = []
li_mod = []
for i in range(0, 10):  # 숫자 10개를 입력
  a = int(input())
  li.append(a)
  li_mod.append(a%42)
li_mod = set(li_mod)
print('\n')
len(li_mod)