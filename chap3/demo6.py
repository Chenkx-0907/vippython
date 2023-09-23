# 单 位：浙江大学
# 姓 名：陈可鑫
# 开发时间：2023/9/23 18:57
# 布尔运算符
a,b = 1,2
print('-----------and 并且------------')
print(a==1 and b==2)    #True
print(a==1 and b<2)     #False
print(a!=1 and b==2)    #False
print(a!=1 and b!=2)    #False

print('-----------or 或者------------')
print(a==1 or b==2)    #True
print(a==1 or b<2)     #True
print(a!=1 or b==2)    #True
print(a!=1 or b!=2)    #False

print('-----------not 对bool类型的操作数取反------------')
f = True
f2 = False
print(not f)
print(not f2)

print('-----------in 与 not in-------------')
s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)