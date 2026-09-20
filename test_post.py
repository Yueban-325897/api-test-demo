import requests

def test_post_demo():
    # 1. 准备网址（和Postman里填的一模一样）
    url = "http://httpbin.org/post"
    
    # 2. 准备要提交的数据（用Python的字典，完美对应JSON）
    my_data = {"name": "cxm" , "age": "24"}
    
    # 3. 发送POST请求（相当于Postman选POST，填Body，点Send）
    response = requests.post(url, json=my_data)
    
    # 4. 断言：检查状态码是不是200
    assert response.status_code == 200
    
    # 5. 打印服务器返回的数据（看看它有没有把数据退给我们）
    print("发送的数据：", my_data)
    print("服务器返回的结果：", response.json())

if __name__ == "__main__":
    test_post_demo()