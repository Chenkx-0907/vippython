# 单 位：浙江大学
# 姓 名：陈可鑫
# 开发时间：2023/9/23 18:40
# 比较运算符,比较运算符的结果类型为bool类型
a,b = 10,20
print('a>b吗?',a>b)     #False
print('a<b吗？',a<b)      #True
print('a<=b吗？',a<=b)    #True
print('a>=b吗？',a>=b)    #False
print('a==b吗？',a==b)    #False
print('a!=b吗？',a!=b)    #True

'''一个 = 成为赋值运算符，两个 = 成为比较运算符
    一个变量有三部分组成，标识、值、类型
    == 比较的是值value
    比较对象的标识使用的是 is
'''

a=10
b=10
print(a==b)     #True   说明a与b的值value相等
print(a is b)   #True   说明a与b的id标识相等

#以下代码没学过，后续会讲解
list1 = [11,22,33,44]
list2 = [11,22,33,44]
print(list1 == list2)       #-->True
print(list1 is list2)       #-->False
print(id(list1))
print(id(list2))

print(a is not b)               #False
print(list1 is not list2)       #True