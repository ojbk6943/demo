# 获取 admin 用户的token
# import requests
#
# url="http://localhost/kodexplorer4.40/?user/loginSubmit&isAjax=1&getToken=1&name=admin&password=admin"
# resp=requests.get(url)
# data=resp.json()
# print(data)
# print(type(data))
# print(data['data'])

#不登录 不使用accessToken参数获取用户名为demo的信息
# import requests
# import json
# url="http://192.168.2.187/kodexplorer4.40/?systemMember/getByName"
# data={"name":"demo"}
# resp=requests.post(url,data)
# print(resp.status_code)
# print(resp.text)
# # data=resp
# # print(data)
# #不登录  使用demo账号token获取demo用户的信息
# #1.获取demo的token
# import requests
#
# url="http://192.168.2.187/kodexplorer4.40/?user/loginSubmit&isAjax=1&getToken=1&name=demo&password=demo"
# resp=requests.get(url)
# data=resp.json()
# # print(data)
# # print(type(data))
# # print(data['data'])
# demo_token=data['data']
# # print(demo_token)
# #获取用户的信息
# url="http://192.168.2.187/kodexplorer4.40/?systemMember/getByName"
# data1={"name":"demo","accessToken":demo_token}
# resp=requests.post(url,data=data1)
# # print(resp.text)
# print(resp.json())
# print(resp.status_code)
# print(resp.text)





#不登录 使用admin账号的token 获取demo用户的信息
import requests

url="http://192.168.2.187/kodexplorer4.40/?user/loginSubmit&isAjax=1&getToken=1&name=admin&password=admin"
resp=requests.get(url)
data=resp.json()
# print(data)
# print(type(data))
# print(data['data'])
admin_token=data['data']
# print(demo_token)
#获取用户的信息
url="http://192.168.2.187/kodexplorer4.40/?systemMember/getByName"
data1={"name":"demo","accessToken":admin_token}
resp=requests.post(url,data=data1)
# print(resp.text)
print(resp.json())
print(type(resp.json()))
print(resp.status_code)


