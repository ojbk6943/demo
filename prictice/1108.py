# import requests
# import time
# url1="http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather"
# data1={"theCityCode":"宝鸡","theUserID":""}
# resp=requests.post(url=url1,data=data1)
# time.sleep(2)
# print(resp.text)
# #断言
# if '宝鸡' in resp.text:
#     print('测试成功')
# else :
#     print('测试失败')
#

import websocket,time,threading
def when_message(ws,message):
    print('接受到的信息：' + message)
def when_open(ws):
    print('建立连接')
    def run():
        while True:
            msg=input("请输入内容：你好啊")
            ws.send(msg)
            time.sleep(1)

            #如果用户输入close消息，则直接关闭本次连接
            if msg=='close':
                ws.close()
                break
    threading.Thread(target=run).start()
#当连接关闭时，会触发on_close事件运行，并运行相应代码
def when_close(ws):
    print('连接关闭')
#建立与服务器端的连接，并指定对应事件调用的对应函数名
ws=websocket.WebSocketApp('ws://echo.websoket.org',on_message=when_message,on_open=when_open,on_close=when_close)
#保持永久连接
ws.run_forever()