# 单 位：浙江大学
# 姓 名：陈可鑫
# 开发时间：2023/9/21 18:00
a = 3.14159
print(a,type(a))
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)
print(n1+n3)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))