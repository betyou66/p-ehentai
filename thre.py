import os,re,asyncio,contextvars,threading,time,ssl,socket,io
from bs4 import BeautifulSoup
ba = BeautifulSoup

'''
不干扰主线程的子进程操作
子线程使用多线程对数据进行改变
当改变完成发送信号
主进程监听状态
'''
start_time = time.time()

async def data(s,fu):
        da = b""
        while True:
            d = s.recv(1024)
            da += d
            if(len(d)==5):
                #print(da.decode())
                fu.set_result(da)
                break
class R:
    def get(self,r):
        #print(r.result().decode())
        pass
    def __init__(self):
        self.context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.context.check_hostname = False
        self.context.set_alpn_protocols(["http/1.1","spdy/2"])
        #e-hentai.org 104.20.135.21
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('104.20.135.21',443))
        self.loop = asyncio.new_event_loop()
        #asyncio.set_event_loop(self.loop)
        self.s = self.context.wrap_socket(self.s)

    def connectd(self,path):
        self.fu = asyncio.Future(loop=self.loop)
        self.task = [data(self.s,self.fu)]
        self.s.send(b"GET "+path.encode("utf-8")+b" HTTP/1.1\r\nHost: "+'e-hentai.org'.encode("utf-8")+b"\r\nUser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nConnection: keep-alive\r\n\r\n")
        self.fu.add_done_callback(self.get)
        self.loop.run_until_complete(asyncio.wait(self.task))
        self.loop.close()
        return r.fu.result()
r = R()

xia = []
img = []
stat = True#信号
lj = r.connectd('/s/703dc8f1cd/2797963-1')

def getall():
    global lj
    ljs = ba(lj,'html.parser')
    for i in ljs.find_all('a'):
        if('next' in i.decode()):
            if(xia==[]):
                xia.append(i['href'])
        if('id="img"' in i.decode()):
            img.append(i.img["src"])

getall()
zhs = 190
'''
for i in range(189):
    r = R()
    lj = r.connectd(xia[0][20:])
    if(len(xia)==1):
        del xia[0]
    getall()
'''
import requests
url = 'https://jnanarn.spzuzbzwobso.hath.network:62281/h/703dc8f1cdd5c39dd1ca31c3b431f49b6c3e60c4-576188-1200-1672-jpg/keystamp=1705274400-0e1f5f46c7;fileindex=141398597;xres=org/000.jpg'
url2 = 'https://xxgpndo.hllbkeamfide.hath.network:54367/h/cc29dee099ea1947a3702cc32b777d0f82cc6b79-310582-1200-1745-png/keystamp=1705274700-dcd6473fb7;fileindex=141398795;xres=org/193.png'

rs = requests.get(url)
sz = rs.content
print(sz)

rs.close()
rk = requests.get(url2)

rk.close()
hc = sz + rk.content
print(len(hc))
end_time = time.time()
 
# 计算并打印运行时间（单位：秒）
run_time = end_time - start_time
print(f"代码运行时间为: {run_time} 秒")