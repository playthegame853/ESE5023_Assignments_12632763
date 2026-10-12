# 定义矩阵，五列十行和十行五列
import random
M1=[]
for i in range(5):
    hang=[]
    for i1 in range(10):
        a=random.randint(0,50)
        hang.append(a)
    M1.append(hang)
M2=[]
for i in range(10):
    hang1=[]
    for i2 in range(5):
        b=random.randint(0,50)
        hang1.append(b)
    M2.append(hang1)
# 定义矩阵
def matrixmultip(A,B):
    m=len(A)
    n=len(B)
    p=len(B[0])
# 创建结果矩阵，初始全部为0
    result=[]
    for i in range(m):
        hang2=[]
        for i3 in range(p):
            hang2.append(0)
        result.append(hang2)
# 矩阵运算
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total = total + A[i][k] * B[k][j]
            result[i][j] = total
    return result
# 调用函数及输出
result = matrixmultip(M1, M2)
print("M1 = ")
for r in M1:
    print(r)
print("M2 = ")
for r in M2:
    print(r)
print("M1 * M2 = ")
for r in result:
    print(r)