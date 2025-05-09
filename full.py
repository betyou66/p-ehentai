import socket,ssl,re,urllib.parse,requests
class Prx:
    '''
    这个类可以通过连接ip发送底层请求，如果ip没有被封禁
    :param hostname: 域名
    :param path: 查询路径
    :param dats: 接收的数据以字节形式返回
    '''
    def __init__(self,url:str,target_ip:str,headers:dict):
        self.url = url
        self.path = '/'
        self.sockets = ''
        self.htmldata = b''
        self.target_ip = target_ip
        #ssl certificate
        self.context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.context.options |= ssl.PROTOCOL_TLSv1_1
        self.context.options |= ssl.PROTOCOL_TLSv1
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.context.check_hostname = False
        self.context.set_alpn_protocols(["http/1.1","spdy/2",'TLS/1.2'])
        self.context.keylog_filename = "./key.log"
        self.__localhost = '127.0.0.1'
        self.headers=headers
    #自定义客户端ip

    def __doc__(self):
        pass
    def pase(self):
        self.path = self.url.split('//')[1].split('/')
        self.path =  '/'+'/'.join(self.path[1:len(self.path)])
        print(self.path)


    def data(self):
        while True:
            try:
                data = self.sockets.recv(4096)
                self.htmldata += data
                self.htmldata = self.htmldata.split(b'\r\n')[7].split(b': ')[1].decode()
                break
            except Exception as e:
                print(e)
                break
        return self.htmldata
    def sends(self):
        if(self.target_ip!=None):
            print('None')
            s = socket.create_connection((self.target_ip,443))

            ss = self.context.wrap_socket(s,server_hostname=self.target_ip)
            ck = 'Cookie: ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; sk=bp8w6rdgmeci934fp919r6m7zp99;'
            if('fullimg' in self.path):
                print('fullimg')
                sends=f'''GET {self.path} HTTP/1.1\r\nHost: e-hentai.org\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nConnection: keep-alive\r\n{ck}\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nPriority: u=4\r\nReferer: https://forums.e-hentai.org/\r\nPragma: no-cache\r\nCache-Control: no-cache\r\n\r\n'''



            #print(sends.encode())
            ss.send(sends.encode())
            self.sockets = ss
            dli = self.data()
            ss.close()
            dirs = self.url.split('/')[-4]
            return self.url.split('/')[-1],dli,dirs



#p = Prx('https://e-hentai.org/fullimg/3104091/1/fhh3n79aee4/a_00.png','104.20.19.168',{})
#p.pase()
#print(p.sends())

