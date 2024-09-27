# -*- coding: utf-8 -*-
from collections.abc import Callable, Iterable, Mapping
import http.server,ssl,re,threading,os,bs4,asyncio,queue,linkall
import multiprocessing
from typing import Any
import lxs
from urllib import parse
dul = queue.Queue()
result = os.popen('ifconfig').read()
st1 = result.find('inet',100)
ks = result[st1:].find(' ')+1
end = result[st1:].find('  ')
jg = result[st1:]
jywip = jg[ks:end]
print(ks)
class MyHandler(http.server.SimpleHTTPRequestHandler):
    search = ""
    tf = True
    def download(self):
        '''
        :根据正则匹配图片地址下载图片
        '''
        pass
    #directory = "C:/dow/stable-diffusion-webui/一些小脚本/pix/server"

    def do_GET(self):
        #self.request是套接字
        print(self.client_address)
        self.directory = "./server"
        inps = [self.server]
        self.send_response(200)
        self.end_headers()
        print(threading.active_count())
        #告诉客户端文件类型
        nt = ""
        if(re.search(r"(.css|.js|.ico)",self.path)==None):
            nt = ".html"
        else:
            nt = re.search(r"(.css|.js|.ico)",self.path).group()
        houzui = [".html",".css",".js",".ico"]
        sci = 0
        hasattr = [self.send_header('Content-type', 'text/html;charset=utf-8;*/*'),self.send_header('Content-type', 'text/css;charset=utf-8;*/*'),self.send_header('Content-type', 'text/javascript;charset=utf-8;*/*'),self.send_header('Content-type', 'image/x-icon;')]
        def scq(hz,zhi):
            for i in range(len(hz)):
                if(hz[i] is zhi):
                    yield hasattr[i]
        for i in scq(houzui,nt):
            i

        #使用select
       
            

        lxs.Prx.url = "https://e-hentai.org"+self.path
        #lxs.Prx.url = "https://www.pixiv.net"+self.path
        #lxs.Prx.url='https://www.pixiv.net'+self.path
        
        sta = lxs.Prx()
        sta.pase()

        #sta.ipw = '172.64.145.17'
        sta.ipw = '104.20.19.168'


        #sta.query = re.sub(r"\?next=","",sta.query)
        #sta.query = re.sub(r"\?p=","",sta.query)
        if(os.path.isfile("./server/"+sta.query+sta.types)):
            match sta.types:
                case ".html":
                    self.send_header('Content-type', 'text/html;charset=utf-8;*/*')
                case ".css":
                    self.send_header('Content-type', 'text/css;charset=utf-8;*/*')
                case ".js":
                    self.send_header('Content-type', 'text/javascript;charset=utf-8;*/*')
                case ".ico":
                    self.send_header('Content-type', 'image/x-icon;')
                case '.img':
                    self.send_header('Content-type', 'image/*;')
                case '.jpg':
                    self.send_header('Content-type', 'image/jpeg;')
            self.wfile.write(open("./server/"+sta.query+sta.types,"rb").read())
            self.request.close()
            #print(open("C:/dow/stable-diffusion-webui/一些小脚本/pix/server/"+sta.query+sta.types,"rb").read().decode('shift-jis'))
        else:
            #sta.query = wjm[len(wjm)-1]
            match sta.types:
                case ".html":
                    self.send_header('Content-type', 'text/html;charset=utf-8;*/*')
                case ".css":
                    self.send_header('Content-type', 'text/css;charset=utf-8;*/*')
                case ".js":
                    self.send_header('Content-type', 'text/javascript;charset=utf-8;*/*')
                case ".ico":
                    self.send_header('Content-type', 'image/x-icon;')
                case '.img':
                    self.send_header('Content-type', 'image/*;')
                case '.jpg':
                    self.send_header('Content-type', 'image/jpeg;')
                case "":
                    sta.types = ".html"
                    self.send_header('Contet-type', 'text/html;charset=utf-8;*/*')
            if self.path == "/":
                sta.types = ".html"
            else:
                filename,dil = sta.sends()
                print(2)

                #we = bs4.BeautifulSoup(open("pix/server/"+sta.query+sta.types,"rb").read(),"html.parser")
                we = bs4.BeautifulSoup(dil,"html.parser")
                try:
                    print(str(we.find_all('span')[0]).split('>'))
                    if(we.find_all('span')[0]==b''):
                        print('span []')
                        #self.wfile.write(open("C:/dow/stable-diffusion-webui/一些小脚本/pix/server/"+sta.query+sta.types,"rb").read())
                        self.wfile.write(dil)
                        self.request.close()
                    else:
                        
                        pass
                        '''
                        创建一个网页副本用来更新
                        然后将副本写入客户端
                        '''
                        '''
                        open("pix/server/"+'a'+sta.query+sta.types,"w")
                        open("pix/server/"+'a'+sta.query+sta.types,"wb").write(open("pix/server/"+sta.query+sta.types,"rb").read())
                        spl = "pix/server/"+'a'+sta.query+sta.types
                        '''

                        #添加websocket
                        #'const socket = new WebSocket("ws://127.0.0.1:8001");socket.addEventListener("message", function (event) {\r\nasync function cs(blob){\r\nconst text = await new Response(blob).text();document.innerHTML = text;\r\n}\r\ncs(event.data)});\r\nsocket.send('+'a'+sta.query+sta.types+')\r\n'
                        #插入js异步
                        '''
                        xiugai = open("pix/server/"+sta.query+sta.types,"rb").read()
                        fb = xiugai.decode('utf-8').split('\r\n')
                        fb.insert(5,'<script>const socket = new WebSocket("ws://127.0.0.1:8001");\r\nsocket.addEventListener("message", function (event) {\r\nasync function cs(blob){\r\nconst text = await new Response(blob).text();\r\ndocument.body.innerHTML = text;\r\n}\r\ncs(event.data)});\r\nfunction se(){\r\nsocket.send("'+'a'+sta.query+sta.types+'")};\r\nwindow.setInterval(func=se,6000)\r\n</script>')
                        fuben = '\r\n'.join(fb)
                        '''
                        self.wfile.write(dil)
                        #self.wfile.write(fuben.encode('utf-8'))
                        #multiprocessing.Process(linkall.qs("./server/"+sta.query+sta.types,"./server/"+'a'+sta.query+sta.types)).start()
                        
                        

                except:
                    self.wfile.write(open("./server/"+sta.query+sta.types,"rb").read())
                    #linkall.stars("./server/"+sta.query+sta.types)
                    #linkall.stars("./server/"+self.query+self.types)
                    #self.request.close()
        if self.path == "/":
            match sta.types:
                case ".html":
                    self.send_header('Content-type', 'text/html;charset=utf-8;*/*')
                case ".css":
                    self.send_header('Content-type', 'text/css;charset=utf-8;*/*')
                case ".js":
                    self.send_header('Content-type', 'text/javascript;charset=utf-8;*/*')
                case "ico":
                    self.send_header('Content-type', 'image/x-icon;')
                case "":
                    sta.types = ".html"
                    self.send_header('Content-type', 'text/html;charset=utf-8;*/*')

            if(os.path.isfile("./server/index.html")):
                self.wfile.write(open("./server/index.html","rb").read())
                self.request.close()
            else:
                f,d = sta.sends()
                #self.wfile.write(open("C:/dow/stable-diffusion-webui/一些小脚本/pix/server/index.html","rb").read())
                self.wfile.write(d)
                #linkall.stars("./server/"+sta.query+sta.types)
                #linkall.stars("./server/"+self.query+self.types)
                    

                #self.request.close()
 
        #print(sta.query,sta.types)



            #self.inpus.append()
            #这里会将所有文件一起发过去
        #
'''
<script async src="//adserver.juicyads.com/js/jads.js"></script>
				<ins id="265909" data-width="728" data-height="90"></ins>
				<script>(adsbyjuicy = window.adsbyjuicy || []).push({'adzone':265909});</script>

                <script async src="//adserver.juicyads.com/js/jads.js"></script><ins id="249007" data-width="728" data-height="90"></ins>
					<script>(adsbyjuicy = window.adsbyjuicy || []).push({'adzone':249007});</script>
					<div id="i4">
						<div>001.jpg :: 1280 x 1806 :: 274.9 KiB</div>
                        
                        根据span标签获取多少页然后轮询
                        获取img标签为id的保存
                        然后其他标签全部删除
                        如果存在span则使用这个方法递归所有网页获取
                        图片标签为img id也是img
'''
            
        
def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    print('ip ','127.0.0.1')
    server_address = ('127.0.0.1', 8000)
    #context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #context.load_cert_chain(certfile="C:\dow\stable-diffusion-webui\一些小脚本\pix\zs\localhost.pem",keyfile="C:\dow\stable-diffusion-webui\一些小脚本\pix\zs\localhost.key")
    #context.load_cert_chain(certfile="C:\dow\stable-diffusion-webui\一些小脚本\pix\zs\localhost.pem",keyfile="C:\dow\stable-diffusion-webui\一些小脚本\pix\zs\localhost.key")
    httpd = server_class(server_address,handler_class)
    httpd.socket = httpd.socket
    httpd.allow_reuse_address = True
    ser = threading.Thread(target=httpd.serve_forever())
    #httpd.serve_forever()
    #ser.setDaemon(True)
    ser.start()

run()
 
#清除服务器缓存
def dele():
    for i in os.listdir('./server'):
        if(re.search(r'(.html)',i)==None):
            pass
        else:
            os.remove('./server/'+i)
dele()
 
