# 单 位：浙江大学
# 姓 名：陈可鑫
# 开发时间：2023/9/19 19:43
# 转义字符
print('hello\nworld')   # \ +转义功能的首字母   n-->newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')   #world对hello进行了覆盖
print('hello\bworld')   #\b是退一个格，把o退没了


print('http:\\\\baidu.com')
print('老师说：\'大家好\'')


# 原字符不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或者R
print(r'hello\nworld')
print(R'hello\nworld')
# 注意事项，最后一个字符不能是\
# print(r'hello\nworld\')
print(r'hello\nworld\\')