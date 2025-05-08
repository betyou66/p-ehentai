
import socket,ssl,re,urllib.parse,requests

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
    def __init__(self,url:str,target_ip:str,headers:dict):
        self.url = url
        self.__localhost = '127.0.0.1'
        self.path = '/'
        self.dats = b''
        self.query = ''
        self.types = ''
        self.sockets = ''
        self.docunetpool = []
        self.target_ip = target_ip
        #ssl certificate
        self.context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.context.options |= ssl.PROTOCOL_TLSv1_1
        self.context.options |= ssl.PROTOCOL_TLSv1
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.context.check_hostname = False
        self.context.set_alpn_protocols(["http/1.1","spdy/2",'TLS/1.2'])
        self.context.keylog_filename = "./key.log"
        self.fenk = ""
        self.__localhost = '127.0.0.1'
        self.headers=headers
        self._mg = ''
        self.sou_addr = ''
        self.htmldata = b''
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


    def data(self):
        '''
        处理数据
        '''
        while True:
            try:

                data = self.sockets.recv(4096)

                #print(data.encode())
                self.htmldata += data
                print(self.htmldata.decode())
                self.htmldata = self.htmldata.split(b'\r\n')[7].split(b': ')[1].decode()

                break

            except Exception as e:
                print(e)
                break
        return self.htmldata
        #数据类型


    def sends(self):



        '''
        发送请求
        两个return

 文件名和文件数据
        '''


        if(self.target_ip!=None):
            print('None')
            s = socket.create_connection((self.target_ip,443))

            ss = self.context.wrap_socket(s,server_hostname=self.target_ip)
            ck = 'Cookie: ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; sk=bp8w6rdgmeci934fp919r6m7zp99;'
            cks = ['Cookie: ipb_member_id=7498513; ipb_pass_hash=e36bf990b97f805acb2dd5588440c203; sk=nf32h71b404ktqkgsgq2qgozdcfc;','Cookie: ipb_member_id=5191636; ipb_pass_hash=544b6a81f07d356f3753032183d1fdfb; sk=9cqnaiva7o3feybrrs2qk8feawhn;','Cookie: ipb_member_id=7317440; ipb_pass_hash=dbba714316273efe9198992d40a20172; sk=l4j3radd014zrmdxr2lxpn1mwhwx;']
            if('fullimg' in self.path):
                sends=f'''GET {self.path} HTTP/1.1\r\nHost: e-hentai.org\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nConnection: keep-alive\r\n{ck}\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nPriority: u=4\r\nPragma: no-cache\r\nCache-Control: no-cache\r\n\r\n'''
            else:
                sends=f'''GET {self.path} HTTP/1.1\r\nHost: e-hentai.org\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nPriority: u=4\r\nPragma: no-cache\r\nCache-Control: no-cache\r\n\r\n'''



            #print(sends.encode())
            ss.send(sends.encode())
            self.sockets = ss
            dli = self.data()
            ss.close()
            dirs = self.url.split('/')[-4]
            return self.query+self.types,dli,dirs



#p = Prx('https://e-hentai.org/fullimg/3249396/1/4meyyjzaedm/_001.png','104.20.19.168',{})
#p.pase()
#print(p.sends())

#asyncio.run(cs.sends())
