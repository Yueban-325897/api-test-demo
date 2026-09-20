# ========== 函数2：力扣第一题（两数之和）==========
def two_sum(): #新建一条用例
    nums = [3, 2, 4] #定义数组num
    target = 6 # 定义目标值
    
    for i in range(len(nums)): #range 整数数列，参数要求数字而不是列表
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print("找到了，下标是：", [i, j])


def mx_two_sum():
    nums = [2,7,11,15]
    target = 9
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+ nums[j] == target:
                print("下标：",[i,j])

# ========== 主程序：控制今天跑哪个函数 ==========
if __name__ == "__main__":
    # 想跑哪个，就把前面的 # 删掉（取消注释）。不想跑的，前面加上 # 

    #two_sum()  # 运行两数之和
    mx_two_sum()