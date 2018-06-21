
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# Python提供了pickle模块来实现序列化。

# 首先，我们尝试把一个对象序列化并写入文件：

import pickle

# 字典
d= dict(name='bob',age=20,score=88)
# 序列化成一个bytes
print(pickle.dumps(d)) 

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
with open('D:/python/xuliehua','wb') as f: # 写二进制文件用wb
    pickle.dump(d,f)

# 将序列化的内容从文件读取出来
with open('d:/python/xuliehua','rb') as f:
    d= pickle.load(f)
    print(type(d))  # dict  存的什么,这里就是什么


# JSON

# JSON和Python内置的数据类型对应如下 ![](http://olg7c0d2n.bkt.clouddn.com/18-6-2/46647934.jpg)

import json

# 序列化为json
d = dict(name='bob',age=20,score=99)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
print(json.dumps(d)) 

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"name": "bob", "age": 20, "score": 99}'
print(json.loads(json_str))

# JSON进阶  

# 序列化对象  该对象必须是可序列化的
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('bob',20,99)
# print(json.dumps(s)) # TypeError: Object of type 'Student' is not JSON serializable

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print(json.dumps(s,default=student2dict))

# 重点:不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s,default=lambda obj:obj.__dict__))

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__(限制扩展属性的)的class。

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str =  '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student)) # <__main__.Student object at 0x006639B0>

# 默认是False
obj = dict(name='小明',age=20)
s = json.dumps(obj,ensure_ascii=True) #  
print(s) # {"name": "\u5c0f\u660e", "age": 20}
s = json.dumps(obj,ensure_ascii=False) # 
print(s) # {"name": "小明", "age": 20}
s = json.dumps(obj)
print(s) # {"name": "\u5c0f\u660e", "age": 20}