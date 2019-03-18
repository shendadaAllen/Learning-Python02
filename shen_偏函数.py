import functools
int16 = functools.partial(int, base=16)
# 以后int16就是16进制的数子类型了
print(int16("100"))
