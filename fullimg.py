import lxs,re,socket,requests,threading,os
o = []


class Full(lxs.Prx):
    def data(self):
        while True:
            #try:
            data = self.sockets.recv(4096).decode()
            self.htmldata += data
            o.append(re.search(r"location: (.*?)\r\n",self.htmldata).group(0).split(" ")[1].split("\r\n")[0])
            #except Exception as e:
            if("\r\n\r\n" in data):
                break
                #print(e)
            #open("pix/server/"+self.query+self.types,"ab").write(data)
            #if(len(data)==5):
            #    break
            #if(data==b''):
            #    break
    def sends(self):
        if(self.ipw!=None):
            s = socket.create_connection((self.ipw,443))
            
            ss = self.context.wrap_socket(s,server_hostname=self.ipw)
            #ss = ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_TLSv1_2)
            ss.send(b"GET "+self.path.encode("utf-8")+b" HTTP/1.1\r\nHost: "+self.hostname.encode("utf-8")+b'''\r\nUser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nConnection: keep-alive
Cookie: ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; ipb_session_id=8f2208f24aac08bc9572e004b15efdd5; sk=bp8w6rdgmeci934fp919r6m7zp99;\r\n\r\n''')
            self.sockets = ss
            dli = self.data()
            return self.query+self.types,dli
        pass
list = open("./fullimg.txt","rb").read()
lists = list.decode().split("\r\n")
del lists[len(lists)-1]
all = []
fill = ""
for i in range(len(lists)):
    try:
        Full.url = lists[i].split("\"")[1]
        Full.ipw = "104.20.19.168"
        
        s = Full()
        fill = s.url.split("/")[4]
        
        
        s.pase()
        finame,data = s.sends()
        s.url = o[0]
        all.append(s.url)
        del o[0]
    except Exception as e:
        print(e)
        pass

try:
    os.mkdir("./"+fill)
except:
    pass
err = []
def d(url):
    try:
        r = requests.get("https://cs.sduoi.top/"+url,timeout=100,stream=True,verify=False)
        img = url.split("/")
        open("./"+fill+"/"+img[len(img)-1],"wb").write(r.content)
        r.close()
    except Exception as e:
        #print(e)
        pass
xc = []
for i in range(len(all)):
    xc.append(threading.Thread(target=d,args=(all[i],)))
for i in range(len(xc)):
    xc[i].start()
np = open('./fullimg.txt','wb')
np.write("")
np.close()