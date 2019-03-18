import collections
# deque
q = collections.deque(["a","b","c"])
q.append("d")
print(q)
q.appendleft("x")
print(q)

# namedtuple
circle = collections.namedtuple("Circle", ["x", "y", "z"])#圆
c = circle(10, 20, 30)
print(c)

#Counter 统计字符串个数

c = collections.Counter("abcdefgabcdeabcdabcaba")
print(c)
# 打印这么一串玩意Counter({'a': 6, 'b': 5, 'c': 4, 'd': 3, 'e': 2, 'f': 1, 'g': 1})


