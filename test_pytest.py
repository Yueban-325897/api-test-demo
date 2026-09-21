import requests

# Pytest 的唯一硬性规定：测试函数的名字必须以 test_ 开头
def test_post_demo():
    url = "http://httpbin.org/post"
    # 准备要发送的数据（JSON格式）
    my_data = {"username": "chenxueimei", "age": 24}
    
    # 发送POST请求
    response = requests.post(url, json=my_data)
    
    # 断言1：检查状态码是不是200
    assert response.status_code == 200
    
    # 断言2：检查服务器返回的json里，username是不是我们刚刚传进去的
    assert response.json()["json"]["username"] == "chenxueimei"