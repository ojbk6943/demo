import http.client
import json

class AgileoneTest:
    # 初始化，主体、端口号
    def __init__(self):
        self.host = '192.168.2.201'
        self.port = 80
        self.cookie = ''
    # 得到打开首页的cookie
    def open_login(self):
        con = http.client.HTTPConnection(self.host,self.port)
        con.request("GET",'/agileone/')
        login_cookie = con.getresponse().getheader('Set-Cookie')
        print(login_cookie)
        cookie = login_cookie.split(";")[0]
        self.cookie += cookie + ";"
        print(self.cookie)

    def test_login(self):

        con = http.client.HTTPConnection(self.host, self.port)
        #参数
        body_data = 'username=admin&password=admin&savelogin=true'
        header = {'Content-Type':'application/x-www-form-urlencoded','Cookie':self.cookie}
        con.request('POST','/agileone/index.php/common/login/',body=body_data.encode('utf-8'),headers=header)
        rsp = con.getresponse()

        content = rsp.read().decode('utf-8')
        print(content)
        if content == 'successful':
            print("登陆成功")
        else:
            print("登陆失败")
        #捕获cookie
        for info in rsp.getheaders():
            if info[0] == 'Set-Cookie':
                self.cookie += info[1].split(";")[0] +";"
    # 公告管理，新增/index.php/notice/add HTTP/1.1
    def test_add(self):
        random_num = self.get_random()
        # 正文、请求头
        con = http.client.HTTPConnection(self.host, self.port)
        body_data = 'headline=这是第%d标题&content=这是%d内容&scope=1&expireddate=2020-02-04'%(random_num,random_num)
        header = {'Content-Type': 'application/x-www-form-urlencoded','Cookie':self.cookie}
        con.request("POST",'/agileone/index.php/notice/add',body=body_data.encode('utf-8'),headers=header)
        notice_add_res = con.getresponse()
        content = notice_add_res.read().decode()
        # 字符串断言
        if content.isdigit():
            print("公告管理新增字符串校验成功")
        else:
            print("公告管理新增字符串校验失败")
        # 验证数字编号大于12,断言
        if int(content) > 12:
            print("公告管理新增数字校验成功")
        else:
            print("公告管理新增数字校验成功失败")

        # 利用搜索进行断言 http://192.168.2.201/agileone/index.php/notice/query HTTP/1.1
        query_con = http.client.HTTPConnection(self.host,self.port)
        param = "currentpage=1&noticeid=%s&headline=&content=&creator=admin&scope=1&expireddate=2020-02-04"%(content)
        header = {'Content-Type': 'application/x-www-form-urlencoded','Cookie':self.cookie}
        query_con.request('POST','/agileone/index.php/notice/query/',body=param.encode('utf-8'),headers=header)
        query_content = query_con.getresponse().read().decode()
        # 序列化
        query_content_json = json.loads(query_content)
        # 从正文中，对比内容
        headline = query_content_json[0]['headline']
        headline_content = query_content_json[0]['content']
        if headline == '这是第%d标题'%(random_num) and headline_content == '这是%d内容'%random_num:
            print("公告管理新增查询校验成功")
        else:
            print("公告管理新增查询校验失败")

        # 数据库断言


    # 随机数,1-100
    def get_random(self):
        from random import randint
        return randint(1,100)

if __name__ == '__main__':
    at = AgileoneTest()
    at.open_login()
    at.test_login()
    at.test_add()
