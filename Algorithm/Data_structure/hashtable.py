#!coding:utf-8

"""
哈希表的实现
以下代码摘取自：http://www.cnblogs.com/hanahimi/p/4765265.html
"""

class LinearMap(object):
    """ 线性表结构 """
    def __init__(self):
        self.items = []

    def add(self, k, v):    # 往表中添加元素
        self.items.append((k,v))

    def get(self, k):       # 线性方式查找元素
        for key, val in self.items:
            if key==k:      # 键存在，返回值，否则抛出异常
                return val
        raise KeyError

class BetterMap(object):
    """ 利用LinearMap对象作为子表，建立更快的查询表 """
    def __init__(self,n=100):
        self.maps = []          # 总表格
        for i in range(n):      # 根据n的大小建立n个空的子表
            self.maps.append(LinearMap())

    def find_map(self,k):       # 通过hash函数计算索引值
        index = hash(k) % len(self.maps)
        return self.maps[index] # 返回索引子表的引用

    # 寻找合适的子表（linearMap对象）,进行添加和查找
    def add(self, k, v):
        m = self.find_map(k)
        m.add(k,v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)

class HashMap(object):
    def __init__(self):
        # 初始化总表为，容量为2的表格（含两个子表）
        self.maps = BetterMap(2)
        self.num = 0        # 表中数据个数

    def get(self,k):
        return self.maps.get(k)

    def add(self, k, v):
        # 若当前元素数量达到临界值（子表总数）时，进行重排操作
        # 对总表进行扩张，增加子表的个数为当前元素个数的两倍！
        if self.num == len(self.maps.maps):
            self.resize()

        # 往重排过后的 self.map 添加新的元素
        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        """ 重排操作，添加新表, 注意重排需要线性的时间 """
        # 先建立一个新的表,子表数 = 2 * 元素个数
        new_maps = BetterMap(self.num * 2)

        for m in self.maps.maps:  # 检索每个旧的子表
            for k,v in m.items:   # 将子表的元素复制到新子表
                new_maps.add(k, v)

        self.maps = new_maps      # 令当前的表为新表

if __name__=="__main__":
    table = BetterMap()
    pricedata = [("Hohner257",257),
                 ("SW1664",280),
                 ("SCX64",1090),
                 ("SCX48",830),
                 ("Super64",2238),
                 ("CX12",1130),
                 ("Hohner270",620),
                 ("F64C",9720),
                 ("S48",1988)]

    for item, price in pricedata:
        table.add(k=item, v=price)

    print table.get("CX12")
    # >>> 1130
    print table.get("QIMEI1248")
    # >>> raise KeyError