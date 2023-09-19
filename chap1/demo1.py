# 单 位：浙江大学
# 姓 名：陈可鑫
# 开发时间：2023/9/19 19:29
# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('helloworld')
print("helloworld")

# 含有运算符的表达式
print(3+1)

# 将数据输出到文件,注意点：1.指定的盘符存在2.使用file=fp
fp = open('E:/text.txt','a+') # ‘a+’如果文件不存在就创建，有的话就在文件后面继续追加
print('hello world',file=fp)
fp.close()

# 不进行换行输出（输出内容在一行中）
print('hello','world','python')