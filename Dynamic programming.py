def Find_expression(target):
    # 原始数字字符串 "123456789"
    digits = "123456789"
    # 定义递归函数：pos=当前处理到第几位, current_val=当前计算值, current_expr=表达式字符串
    def dfs(pos, current_val, current_expr):
        # 如果走到最后一位（pos ==9）
        if pos == len(digits):
            if current_val == target:
                print(f"{current_expr} = {target}")
            return
        # 取下一个数字，从pos开始，可以往后拼接多位
        num_str = ""
        for i in range(pos, len(digits)):
            num_str = num_str + digits[i]
            num = int(num_str)   
            if pos == 0:
                # 最开头，直接放第一个数字，没有运算符
                dfs(i+1, num, num_str)
            else:
                # 选项1：加号
                dfs(i+1, current_val + num, current_expr + "+" + num_str)
                # 选项2：减号
                dfs(i+1, current_val - num, current_expr + "-" + num_str)
    # 启动递归，从位置0开始
    dfs(0, 0, "")
# 调用测试，题目示例
Find_expression(50)


