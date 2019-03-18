# def a():
#     def b():
#         print("打印b")
#         return "返回值b"
#     return b
#
#
# a = a()
# b = a()
# print(b)
#
# # 闭包遇到的坑
def count():
    l=[]
    for i in range(4):
        def f():
            return i*i
        l.append(f)
    return l
f1,f2,f3,f4 = count()
print(f1())
print(f2())
print(f3())
#
# def count():
#     # 定义列表，列表里存放的是定义的函数
def count():
    l=[]
    for i in range(4):
        def f():
            return i*i
        l.append(f)
    return l
f = count()
l = [i() for i in f]
print(l)
# # print(f4())#结果是四个9
# # # ****************************************
# #修改后的代码
def count2():
    def f(j):
        def g():
            return j*j
        return g
    l = []
    for i in range(1,4):
        l.append(f(i))
    return l

f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())
#
def count():
    def f(j):
        def g():
            return j*j
        return g
    l = []
    for i in range(1,4):
        l.append(f(i))
    return l
f = count()
l = [i() for i in f]
print(l)
#
#
# #改装后的代码
def count2():
    def f(j):
        return j * j
    l = []
    for i in range(1, 4):
        l.append(f(i))
    return l
print(count2())

# 生成一个列表



