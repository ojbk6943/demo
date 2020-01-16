import http.client
if __name__ == '__main__':
    conn=http.client.HTTPConnection('192.168.2.102',8080)                           #获得主机
    login_data='username=admin&password=123456&verifycode=0000'                     #准备参数
    header={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}     #头部
    conn.request('POST','/WoniuSales/user/login',body=login_data,headers=header)    #发送请求
    resp=conn.getresponse()                                                         #
    print(resp.read().decode())
