#-----------------列表----------------
shopping_list = [] #定义一个列表
shopping_list.append("键盘") #添加一个元素
shopping_list.append("显示器") #添加一个元素
shopping_list.remove("键盘") #删除一个元素
shopping_list.append("音响")#添加一个元素
shopping_list.append("电竞椅") #添加一个元素
shopping_list[1] = "硬盘" #替换列表中第2个元素

# print(shopping_list)
# print(len(shopping_list)) #打印列表长度
# print(shopping_list[0]) #打印列表中第一个元素

price = [799,1024,200,800] #定义价格列表
max_price = max(price) #最大值
min_price = min(price) #最小值
# sorted_price = sorted(price) #从小到大排序
# print(max_price)
# print(min_price)
# print(sorted_price)

#------------------字典-----------------
#结合input、字典、if判断，做一个查询流行语含义的电子词典程序
slang_dict = {"觉醒年代":"电视剧",
              "YYDS":"永远的神"}
slang_dict["双减"] = "减负"
slang_dict["破防"] = "情绪"
slang_dict["U1S1"] = "有一说一"

query = input("请输入您想要查询的流行语：")
if query in slang_dict:
    print("您查询的" + query + "含义如下")
    print(slang_dict[query])
else:
    print("您查询的流行语尚未收录。")
    print("当前本词典收录词数："+str(len(slang_dict)) +"条")
print(slang_dict) 