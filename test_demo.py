import requests    # 引入requests外部工具包,用于发送网络请求

def test_get_baidu():  # 定义一条测试用例(起名)  def指新建用例
    url = "https://www.baidu.com"  # 在url变量中存入测试地址
    response = requests.get(url)  # 模拟postman点击send按钮,发get请求,将服务器返回的结果存入response
    assert response.status_code == 200 #断言:检查返回结果中的状态码是不是200
    print("测试通过，百度首页请求成功，状态码：", response.status_code) #打印一句话+状态码

if __name__ == "__main__": # 固定格式,表示直接运行这个文件
    test_get_baidu() # 执行上面这条用例