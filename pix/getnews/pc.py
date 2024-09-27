import socket,ssl
ip = "20.205.243.166"
port = 443
#hostname = "www.torrent9.fm"
hostname = "github.com"
search = 's?wd=图片&rsv_spt=1&rsv_iqid=0xfabaef8c00479456&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&oq=tp&rsv_btype=t&inputT=2317&rsv_t=0515xhq8YHg%2BTjoueZv7tl5md%2BL4%2BR0ZyXvzHIBbLZxGCAn4a1c0HzYg25UVz0lBf2%2Bn&rsv_sug3=9&rsv_sug1=10&rsv_sug7=101&rsv_pq=cd32810900b086b4&rsv_sug2=0&rsv_sug4=2926&bs=tp'
data = b"GET / HTTP/1.1\r\nHost: "+hostname.encode()+b"\r\nUser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,*/*\r\n\r\n"

class Get:
    def __init__(self)->None:
        self.ip = ip
        self.port = port
        self.hostname = hostname
        self.embedding = {1:str}
        self.context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.context.check_hostname = True
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.message = data
        self.search = search
    def get(self)->bytes:
        self.data = b""
        self.connect = socket.create_connection((self.ip,self.port))
        print(self.connect)
        if self.search == '':
            pass
        else:
            self.message = self.search.encode()
        with self.connect as s:
            with self.context.wrap_socket(s,server_hostname=self.hostname) as si:
                print(si.getpeercert())
                si.sendall(self.message)
                while True:
                    datas = si.recv(1024)
                    #print(datas)
                    if not datas:
                        break
                    if(len(datas)==5):
                        print(5)
                        break
                    self.data += datas
                return self.data
print(2.5/6.8)
print(114+19)
'''
s = Get()
s.data = data
s.get()
'''
print(socket.getaddrinfo('baidu.com',443)[0][-1])
#网络拥堵
#查询礼包码自动获取
'''
目标网站
百度
'''
'''
getbaidu = Get()
getbaidu.ip = socket.getaddrinfo('www.baidu.com',443)[0][-1][0]
getbaidu.hostname = "www.baidu.com"
'''
lk = data.decode().split()
lk[1] += search
search = ' '.join(lk)
#print(getbaidu.get())
'''
盘点自身所有的资源
拥有一台电脑
会python但还未完全掌握
会js
还拥有se*资源和网站
多个bt和游戏资源

'''
import socket
sz = [0,1,2,3,4,5,6,7,8,9,10]
sz[0]=123
print(sz)
ca = 'https://e-hentai.org/'
print('https://e-hentai.org' is ca)
zfc = "pix/server/"

print(zfc)
import re
sz = '<img id="img" onerror="this.onerror=null; nl("40513-473585")" onload="update_window_extents()" src="https://hcelpji.iqqnswgedzbf.hath.network:46011/h/983eaa29f4263e44db8b67481d2c05ea9c17ca92-225532-1280-1969-jpg/keystamp=1704908100-6e963357ac;fileindex=116059822;xres=1280/101617315_p0.jpg" style="width:1280px;height:1969px"/>'
print(re.search('onerror',sz).span(0)[0])
print(re.search('src',sz).span(0)[0])
print(sz[14])
print(sz[94])
print(sz[14:94])
print(sz.replace(sz[14:94],''))