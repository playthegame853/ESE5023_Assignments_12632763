def Least_moves(x):
    step = 0  
    current = x  
    # 当还没到初始值1的时候，持续循环
    while current > 1:
        if current % 2 == 1:
            # 如果当前是奇数，上一步只能是+1，反向减1
            current = current - 1
        else:
            # 如果当前是偶数，上一步是乘2，反向除以2
            current = current // 2
        step = step + 1  # 每操作一次，步数+1
    print(step)
# 题目样例测试
Least_moves(2)
Least_moves(5)

