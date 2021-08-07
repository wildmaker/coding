
import random, re
# pick a random word from a text file
def pick_random_word(filename:str ) -> str:
    with open(filename, mode='r') as file:
        text = file.read()
        words = re.sub('[^A-Za-z0-9]+', ' ', text).split()
    return random.choice(words)

# 索引 indexing

greeting = "Hello"

# 基本操作
greeting[0]

# 从后面开始计数
greeting[-1]

# 字符串常量可以直接索引
'Hello'[1]

# 分片 sliceing

tag = '<a href = "http://www.python.org">Python web site</a>'
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 基本操作
tag[11:32]

# 访问最后几个元素
number[-3:]

# 访问前几个元素
number[:3]

# 自定义步长
number[1:6:2]

# 将每几个元素的第一个取出
number[::4]

# 从右往左提取
number[6:2:-2]

# 序列相加
[1,2,3] + [3,4,5]

# 序列相乘
[1,2,3] * 5

# 初始化一定长度的序列
