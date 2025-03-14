import socket,select,ssl,bs4,re,os,urllib.parse,requests

    #e-hentai.org 104.20.135.21
    #upld.e-hentai.org 94.100.18.249
    #hentaiverse.org hentaiverse.org
    #forums.e-hentai.org 104.20.135.21
    #ehgt.org 178.162.139.24
    #await sends("e-hentai.org","/")

class Prx:
    '''
    这个类可以通过连接ip发送底层请求，如果ip没有被封禁
    :param hostname: 域名
    :param path: 查询路径
    :param dats: 接收的数据以字节形式返回
    :param query 保存文件名
    :param types: 保存文件类型
    :param docunetpool 文档名
    :param recursionget 递归文档
    '''
    def __init__(self):
        pass
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = False
    context.set_alpn_protocols(["http/1.1","spdy/2"])
    context.keylog_filename = "./key.log"
    url = ""
    hostname = ""
    path = "/"
    dats = b""
    query = ""
    types = ""
    sockets = ""
    docunetpool = []
    ipw = None
    timeout = 4
    fenk = ""
    __localhost = "127.0.0.1"
    img = ''
    sou_addr = ''
    htmldata = b''
    #自定义客户端ip

    def __doc__(self):
        print("e-hentai.org 104.20.135.21")
        print("upld.e-hentai.org 94.100.18.249")
        print("hentaiverse.org hentaiverse.org")
    def pase(self):
        '''
        解析url
        '''
        
        try:
            result = re.findall(r'([^://]+)',self.url)
            self.hostname = result[1]
            del result[0]
            del result[0]
            fuzhi = result[len(result)-1]
            if(re.search(r"\?",fuzhi)):
                u = re.search(r"=",result[len(result)-1])
                fuzhi = fuzhi.split("=")
                if(re.search(r"\%",fuzhi[1])==None):
                    self.query = fuzhi[1]
                else:
                    self.query = urllib.parse.unquote(fuzhi[1])
            else:
                fge = fuzhi.split(".").pop()
                tio = fuzhi.split("."+fge)
                if(len(tio)<1):
                    self.query=tio.join("")
                else:
                    self.query = tio[0]
            if(re.search(r"\.",result[len(result)-1])==None):
                self.types = ".html"
            else:
                ts = re.findall(r"[^\.]+",result[len(result)-1])
                self.types ='.'+ts[len(ts)-1]
                
            self.path = "/"+"/".join(result)
            if(type(self.hostname)!=str):
                TypeError("hostname must be str")

        except:
            self.query = "index"
            #if(re.search(r"\.",result[len(result)-1])==None):
            #self.types = ".html"
    #匹配path

    def download(self):
        oi = ""
        for i in self.fenk:
            if(re.search(r"https://.*?(keystamp*)",i)==None):
                pass
            else:
                oi = i.split("src=")[1].split("\"")[1]
                filename = oi.split("/")
                filename = filename[len(filename)-1]
                bc = open("pix/server/"+filename,"wb")
                bc.write(requests.get(oi).content)
                bc.close()
                    

    def data(self):
        '''
        处理数据
        '''
        #if os.path.isfile("pix/server/"+self.query+self.types):
           # return True
        while True:
            data = self.sockets.recv(4096)
            self.htmldata +=data
            #open("pix/server/"+self.query+self.types,"ab").write(data)
            if(len(data)==5):
                break
            if(len(data) == b''):
                break
                
        print("开始保存文件","  "+self.query+self.types)
        '''
        self.dats = open("pix/server/"+self.query+self.types,"rb").read()
        da = self.dats.decode("utf-8")
        self.fenk = da.split(" ")
        #threading.Thread(target=self.download).start()
        '''
        da = self.htmldata.decode("utf-8") 
        self.fenk = da.split(" ")                        

        dio = re.sub(r"https://"+self.hostname+r".*?/","http://"+self.__localhost+":8000/",da)
        dio = re.sub(r"http://"+self.__localhost+":8000/z/0372/g.css","http://"+self.__localhost+":8000/g.css",dio)
        dio = re.sub(r"http://"+self.__localhost+":8000/z/0372/ehg_index.c.js","http://"+self.__localhost+":8000/ehg_index.c.js",dio)
        dio = re.sub(r'onerror(.*)?\(\)',"",dio)
        dio = re.sub(r'onload(.*)?\(\)',"",dio)

        '''
            for i in self.fenk:
                if(re.search(r"https://.*?(keystamp*)",i)!=None):
                    ois = i.split("src=")[1].split("\"")[1]
                    filenames = ois.split("/")
                    filenames = filenames[len(filenames)-1]
                    print(i)
                    print(filenames," 图片名字")
                    dio = re.sub(i,"src=\"https://127.0.0.1:8000/"+filenames+"\"",dio)
        '''

        mt = re.search(r"meta",dio)
            #dio = dio[z].format("charset=utf-8")

        da = dio

        cs = da.splitlines()
        ti = 0
        while True:
            del cs[0]
            if ti == 17:
                #print(cs)
                break
            ti+=1
        while True:
            try:
                if(int(cs[len(cs)-1])==0):
                    del cs[len(cs)-1]
                    cs[3]+='\r\n<meta charset="utf-8" />\r\n'
                    #cs.insert(5,'<script>const socket = new WebSocket("ws://127.0.0.1:8001");\r\nsocket.addEventListener("message", function (event) {\r\nasync function cs(blob){\r\nconst text = await new Response(blob).text();\r\ndocument.body.innerHTML = text;\r\n}\r\ncs(event.data)});\r\nfunction se(){\r\nsocket.send("'+"a"+self.query+self.types+'")};\r\nwindow.setInterval(func=se,6000)\r\n</script>')
                    return "\r\n".join(cs).encode("utf-8")
                    #open("pix/server/"+self.query+self.types,"wb+").write("\r\n".join(cs).encode("utf-8"))
                    #删除广告
                    #要删除链接
                    #break

            except:
                del cs[len(cs)-1]
            #print(self.dats)

    def sends(self):

        #socket.setdefaulttimeout(10)

        '''
        发送请求
        两个return
        文件名和文件数据
        '''
        ip = []
        ip.append('172.67.0.127')
        s = socket.create_connection((ip[0],443))
        ss = self.context.wrap_socket(s,server_hostname=ip[0])
        ss.send(b"GET "+self.path.encode("utf-8")+b" HTTP/1.1\r\nHost: "+self.hostname.encode("utf-8")+b"\r\nUser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nConnection: keep-alive\r\n\r\n")
        self.sockets = ss
        dli = self.data()
        return self.query+self.types,dli


    
            #print(self.dats)
#https://e-hentai.org/s/78b98b97e7/2764227-2
#print(Prx.__dict__)


'''
对网页结构的连接处理
'''
#asyncio.run(cs.sends())
