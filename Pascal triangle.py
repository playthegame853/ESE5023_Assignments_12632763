def Pascaltriangle(k):
    # 从第0行开始构造，一直构建到第k行
    current_row = [1]   # 初始：第0行
    for i in range(k):
        new_row = [1]   # 新一行开头永远是1
        # 遍历上一行，相邻两个相加
        for j in range(len(current_row)-1):
            num = current_row[j] + current_row[j+1]
            new_row.append(num)
        new_row.append(1) # 新一行末尾永远是1
        current_row = new_row
    
    print(current_row)
# 调用测试
Pascaltriangle(100)
Pascaltriangle(200)

