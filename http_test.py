"""
 服务端

http 请求响应演示

"""
from socket import *

# 创建套接字tcp
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

while True:
    c,addr=s.accept()
    print("connect from",addr)# 浏览器连接
    data=c.recv(4096)# 接收的是http请求
    print(data.decode().split('\n')[0]) # 请求行

# 响应格式
    web_source = open("index.html")
    html= "HTTP/1.1 200 OK\r\n"
    html+="Content-Type:text/html\r\n"
    html+="\r\n"
    html+=web_source.read()


# 发送响应给客户端
    c.send(html.encode())
    web_source.close()

    c.close()
s.close()

