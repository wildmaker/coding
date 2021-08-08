
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
lst = [None] * 100

# 长度
len(number)

# 最值
max(number)
min(number)

# 基本列表操作
x = [1, 1, 1]

# 赋值
x[1] = 2

# 删除元素
del x[1]

# 分片赋值
number = [1,2,3,4,5,6,7,8,9]
number[1:4] = [6, 6, 6]
# 可以用来插入元素
number[1:1] = ['h','e','l']
# 可以用来删除元素
number[1:3] = []
# 可以用来增加元素
number[len(number):] = ['h','e','l']
# 可以自定义步长
number[1:6:2]=['k', 'l', 'o']

# 列表方法

# append 增加元素到末尾
number.append(10)

# count 统计元素的个数
number.count(6)

# extend 扩展原来的列表
number.extend([10,11,12,13])
# 跟 + 的区别是 extend 改变了原有的列表

# index 查找列表中第一个匹配元素的索引
number.index(6)

# insert 将1个元素插入到列表
number.insert(2, ['a','b','c'])

# pop 从列表末尾中删除一个元素, 返回删除的元素
number.pop()
# 也可删除指定位置的元素
number.pop(1)

# 模拟栈结构：先入后出
# 入栈
number.append("1")
# 出栈
number.pop()

# 模拟队列结构：先入先出
# 入队
number.insert(0,...)
# 出队
number.pop()
# 或者每次都用 pop(0), 入队还用 append, 这样就能做到队列结构

# remove 移除列表中的第一个匹配项
number.remove(6)

# reverse 将列表反向
number.reverse()
# reverse 返回了一个列表，reversed() 函数可以返回一个迭代器
list(reversed(number))

# sort 对列表进行排序, 直接改变对象，不返回值
number.sort()
# 使用 sorted() 函数可以不改变原对象获得排序后的结果
number_1 = sorted(number)

# 还可以自定义排序规则
sort(lambda x,y: 1 if x>y else -1,key = lambda a:a*2,reverse = True)
# 三个参数分别代表：自定义的比较函数、用来排序的键值，是否反向排序
# 自定义的比较函数：返回正数，就把第一个值放后面，返回负数就把第一个值放前面

# tuple

# tuple 的值在定义的时候就需要指定，因为 tuple 不可变更
t = (1, 2)

# 定义只有一个元素的变量时需要带逗号，否则会被 python 视为普通常量
t = ("test") # t = "test", string
t = ("test",) # t = ("test",), tuple

# tuple() 函数，将序列转化为 tuple
tuple('abc')
tuple([1, 2, 3])

# tuple 的元素不可修改，但如果值是可变的，就可以修改（其实变量的指向并没有修改，只是指向的值发生了变化）
t = (1, 2, [3, 4])
t[2][1] = 6

# tuple 的元素不可修改，因此更安全，能用 tuple 的时候尽量用，而不是 list

# dict

# dict的特点：以空间换时间
# 1.访问速度很快，与 dict 的大小无关
# 2.比 list 更占内存

# dict 快速访问的原理
# 对于 dict 中的每个 key, dict 内部都存储了变量唯一的地址（通过 hash 算出），因此每次查找时直接按地址读内存就行了

# 使用注意事项：
# 1.key 值必须为不可变量（否则无法确保地址不变）
# 2.字典中的键值并没有顺序

d = {'albert':'German','wilson':'American'}
d['watlson'] = 'England'

# 避免 key 不存在的错误
# 1.事先检查是否存在
# 2.使用 get() 方法
'Morty' in d
d.get('Morty')

# 删除 key (value 也会一起删除)
d.pop('Morty') # 会返回对应的键值

# set
# set 是一组不重复 key 的集合，可被当作数学上的集合使用
# set 的实现原理和 dict 相似，因此 key 必须不可变
# set 的 key 没有顺序

# 增加值
s = {1, 2, 3}
s.add(6)
s.add(6) # 加重复的 key 不会发生任何事情

