'''
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, 'adasdas  dasdas dasdas dasdas')))

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。


def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列3 5 7 9...
    while True:
        n = next(it)  # 3   取序列第一个数
        yield n
        it = filter(_not_divisible(n), it) # 对it序列进行筛选:x%n>0

'''
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''
# 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

# 练习   回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

# 回文判断
def is_palindrome(n):
    '''   
    下面是我的代码  先转字符串  再判断回文
    numStr = str(n)
    length = len(numStr)
    for i in range(length):
        if numStr[i]!=numStr[length-1-i]:
            return False
    return True
    '''
    return str(n) == str(n)[::-1]  # 倒序切片 666666

output = filter(is_palindrome, range(1, 1000000))
print('1~1000000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。