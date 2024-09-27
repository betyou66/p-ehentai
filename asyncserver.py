import ssl,re,os,queue,linkall,asyncio,time,select,re,socket,lxs,multiprocessing,certifi,threading
result = os.popen('ifconfig').read()
st1 = result.find('inet',100)
ks = result[st1:].find(' ')+1
end = result[st1:].find('  ')
jg = result[st1:]
jywip = jg[ks:end]
print(ks)


class Server:


    def __init__(self):
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        #self.context.load_cert_chain(certfile='C:\dow\stable-diffusion-webui\一些小脚本\cert.pem',keyfile='C:\dow\stable-diffusion-webui\一些小脚本\key.pem')
        #self.server = self.context.wrap_socket(self.server, server_side=True)
        self.server.bind(('127.0.0.1',8000))
        print('ip ',jywip)
        self.server.listen(1000)
        self.dui = queue.Queue()
        self.asy = False
        
    async def send(self,methon,filles,filetype):
        connection = self.dui.get()
        print(self.dui)
        if(filetype.decode('utf-8').split(',')[0] == 'text/html'):
            if(re.search(r"\.",filles) == None):
                filles = filles+'.html'
            if(self.ducu):
                self.filesdata = open('./server/'+filles,'rb').read()
            else:
                self.filesdata = self.alldata


                #删除iframe和一个script块
                lx = re.sub(r'<script async src="//adserver.juicyads.com/js/jads.js"></script>', '', self.filesdata.decode(), flags=re.S)
                #print('文件内容 ',lx)
                self.filesdata = lx.encode('utf-8')
                try:
                    s,t,d,i = linkall.getstartatend(dat=self.filesdata)
                    if(type(t) is int):
                        df = self.filesdata.decode('utf-8')

                        open('./server/url.txt',"ab").write(b"https://e-hentai.org"+self.fillesdir.encode('utf-8')+b'\r\n')
                        
                        print(i.split('"')[3])
                        
                        open("./server/img/url.txt","ab").write(i.split('"')[3].encode("utf-8")+b"\r\n")
                        threading.Thread(target=linkall.main,args=df).start()
                        pass
                except:
                    pass



            self.contextlen = 'Content-Length: '+str(len(self.filesdata))
            self.contextlen = b'\r\n'+self.contextlen.encode('utf-8')
            print('文件长度 ',self.contextlen)
            filetype = b'text/html'
            message =b'HTTP/1.1 200 ok\r\nContent-Type: '+filetype+self.contextlen+b'\r\nCache-Control: max-age=43200\r\n\r\n'+self.filesdata+b'\r\n\r\n'
            
        else:
            self.filesdata = open('./server/'+filles,'rb').read()
            self.contextlen = 'Content-Length: '+str(len(self.filesdata))
            self.contextlen = b'\r\n'+self.contextlen.encode('utf-8')
            print('文件长度 ',self.contextlen)
            message =b'HTTP/1.1 200 ok\r\nContent-Type: '+filetype+self.contextlen+b'\r\nCache-Control: max-age=120\r\n\r\n'+self.filesdata+b'\r\n\r\n'

        #print(message)
        connection.send(message)
        #connection.close()
    
    async def dataanalysis(self,da):
        try:
            self.methon = da[0]
            self.fillesdir = da[1]
            self.filles = da[1].split('/')[-1]
            if(self.filles == ''):
                self.filles = self.fillesdir.split('/')[-2]
            self.filetype = ''
            if(self.fillesdir=='/'):
                self.filles = 'index.html'
            for i in(range(len(da))):
                if(re.search('Accept',da[i])!=None):
                    self.filetype = da[i+1].split('\r\n')[0].encode('utf-8')
                    break
        except:
            pass
            print('error')
    async def searchfile(self):
        '''
        查询文件是否存在
        '''
        self.dir = os.listdir('./server')
        self.wj = ''
        self.ducu = False
        if(re.search(r"\.",self.filles) == None):
            self.filles = self.filles+'.html'
            print(self.filles," self.filles")
            print(self.fillesdir," self.fillesdir")
        if(self.filles in ','.join(self.dir)):
            print('存在')
            self.ducu = True
        if(self.ducu == False):
            print('bcz ',self.fillesdir)


            lxs.Prx.url = "https://e-hentai.org"+self.fillesdir
            lxs.Prx.ipw ='104.20.19.168'
            #lxs.Prx.ipw = '104.244.43.208'

            #lxs.Prx.url = 'https://www.pixiv.net'+self.fillesdir
            #lxs.Prx.ipw = '104.18.42.239'


            sta = lxs.Prx()
            sta.pase()
            finame,data = sta.sends()
            self.filles = finame
            self.alldata = data
            
            self.asy = True
            #await linkall.qs("pix/server/"+self.filles,"pix/server/"+'a'+self.filles)
            print('不存在')
            
        pass
        

    async def run(self):
        print(self.server.accept)
        while True:
            conn,addr = self.server.accept()
            try:
                data = conn.recv(1024)
                socket.setdefaulttimeout(10)
            except:
                print('cw')
            self.dui.put(conn)
            #print(data)
            #获取请求方法
            #获取请求文件
            datasl = data.decode('utf-8').split(' ')
            '''
            for i in range(len(datasl)):
                if(re.search(r'GET|POST|',datasl[i])==None):
                    print(re.search(r'GET|POST|',datasl[i]))
                    pass
                else:
                    
                    methon= re.search(r'(GET|POST|)',datasl[i]).group(1)
            '''
            try:
                await self.dataanalysis(datasl)
                await self.searchfile()
                    #print(self.alldata)      
                await self.send(self.methon,self.filles,self.filetype)
                #print(methon)
                #print(datasl)
            except:
                    print('error')
            
    
    #asyncio.run(self.__init__())
start = Server()
open('./server/cs.html','wb').write(b'')
asyncio.run(start.run())

