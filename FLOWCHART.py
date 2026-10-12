def X(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if b > c:
            print(c, a, b)
        else:
            print(c, b, a)
# 测试随机组
print("测试1: a=5, b=3, c=1")
X(5, 3, 1)

print("测试2: a=5, b=2, c=4")
X(5, 2, 4)

print("测试3: a=2, b=7, c=1")
X(2, 7, 1)

print("测试4: a=1, b=4, c=6")
X(1, 4, 6)

