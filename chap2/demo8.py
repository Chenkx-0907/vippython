# 单 位：浙江大学
# 姓 名：陈可鑫
# 开发时间：2023/9/21 18:13
name='张三'
age=20

print(type(name),type(age))     #说明name与age的数据类型不同
# print('我叫'+name+'今年，'+age+'岁')
print('我叫'+name+'今年，'+str(age)+'岁')     #将int类型通过str()函数转成了str类型

print('------------str()将其他类型转化为str类型')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))


print('------------int()将其他类型转换为int类型')
s1='128'
f1=98.7
s2='76.77'
f2=True
s3='hello'
print(type(s1),type(f1),type(s2),type(f2),type(s3))
print(int(s1),type(int(s1)))    #将str转换为int类型，字符串为数字串
print(int(f1),type(int(f1)))    #将float转换为int类型，截取整数部分，舍去小数部分
# print(int(s2),type(int(s2)))  #将str转换为int类型，报错，因为字符串为小数串
print(int(f2),type(int(f2)))
# print(int(s3),type(int(s3)))  #将str转换为int类型，字符串必须为数字串（整数），非数字串不允许转换


print('------------float()函数，将其他类型转换为float类型')
s1='128.98'
s2='76'
f2=True
s3='hello'
i=98
print(type(s1),type(s2),type(f2),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(f2),type(float(f2)))
# print(float(s3),type(float(s3)))  #字符串中的数据是非数字串，则不能转换
print(float(i),type(float(i)))