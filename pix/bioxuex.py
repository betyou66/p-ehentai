import socket,ssl,select,time,re
def stars(paths,):
     context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
     context.check_hostname = None
     context.verify_mode = ssl.CERT_REQUIRED
     s = socket.create_connection(('104.20.135.21', 443))
     ss = context.wrap_socket(s)
     current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
     outpull = []
     inputs = [ss]
     sj = 1
     sz = []
     djs = 0

     datas = b""

     ss.send(b"GET "+paths.encode("utf-8")+b" HTTP/1.1\r\nHost: e-hentai.org\r\n\r\n")
     print(current_time)
     tz = 0
     while True:
        if(tz==1):
            return datas
        r,w,e = select.select(inputs,outpull,inputs,sj)
        for si in r:
            if si is ss:
                 data = si.recv(1024)
                 if not data:
                      print("Connection closed by remote host")
                      break
                 outpull.append(si)
                 sz.append(data)
            else:
                  data = s.recv(1024)
        for si in w:
            if(range(len(sz))==range(0,0)):
                tz = 1
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            for d in range(len(sz)):
                try:
                    #body
                    if(re.search(r"<!DOCTYPE html>",sz[d].decode("utf-8"))==None):
                        pass
                    else:
                        sz[d]=sz[d].decode("utf-8").replace(sz[d].decode("utf-8")[0:re.search(r"<!DOCTYPE html>",sz[d].decode("utf-8")).span(0)[0]],"")
                    if(re.search(r"body{font-size:8pt",sz[d].decode("utf-8"))==None):
                        pass
                    else:
                        sz[d]=sz[d].decode("utf-8").replace(sz[d].decode("utf-8")[0:re.search(r"body{font-size:8pt",sz[d].decode("utf-8")).span(0)[0]],"")
                    if(re.search(r"function",sz[d].decode("utf-8"))==None):
                        pass
                    else:
                        sz[d]=sz[d].decode("utf-8").replace(sz[d].decode("utf-8")[0:re.search(r"function",sz[d].decode("utf-8")).span(0)[0]],"")
                    print(1)
                    sz[d] = sz[d].encode("utf-8")
                except:
                    pass
                print(d)
                datas=sz[d]
                open("C:\dow\stable-diffusion-webui\一些小脚本\pix\getnews/fg.html", "ab").write(sz[d].encode("utf-8"))
                sz = []
                djs += 1
                outpull.remove(si)
                break    
        for si in e:
            print("Exception occured")
            r.remove(si)
            ss.close()
            break

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

#print(stars("/z/0372/ehg_index.c.js"))
'''


        def stars(self):
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            context.check_hostname = None
            context.verify_mode = ssl.CERT_REQUIRED
            s = socket.create_connection(('104.20.135.21', 443))
            ss = context.wrap_socket(s)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            outpull = []
            inputs = [ss]
            sz = []
            ss.send(b"GET "+self.path.encode("utf-8")+b" HTTP/1.1\r\nHost: e-hentai.org\r\n\r\n")
            print(current_time)
            tz = 0
            while True:
                if(tz==1):break
                r,w,e = select.select(inputs,outpull,inputs)
                for si in r:
                    if si is ss:
                        data = si.recv(1024)
                        if not data:
                            print("Connection closed by remote host")
                            break
                        w.append(self.request)
                        sz.append(data)
                    else:
                        data = s.recv(1024)
                for si in w:
                    if(range(len(sz))==range(0,0)):
                        tz = 1
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        for d in range(len(sz)):
                            try:
                                sz[d]=sz[d].decode("utf-8")
                                if(re.search(r"<!DOCTYPE html>",sz[d])==None):
                                    #sz[d]=sz[d].replace(sz[d][0:451],"")
                                    pass
                                else:
                                    sz[d]=sz[d].replace(sz[d][0:re.search(r"<!DOCTYPE html>",sz[d]).span(0)[0]],"")
                                    sci+=1
                                if(re.search(r"https://e-hentai.org/",sz[d])==None):
                                    pass
                                else:
                                    sz[d]=re.sub(r"https://e-hentai.org/","https://127.0.0.1:8000/",sz[d])
                                sz[d] = sz[d].encode("utf-8")
                                open("C:\dow\stable-diffusion-webui\一些小脚本\pix\getnews/fg.html", "ab").write(sz[d])
                                self.wfile.write(sz[d])
                                w.remove(si)
                                r.remove(ss)
                                break
                            except:
                                self.wfile.write(sz[d])
                            #sz = []   
                for si in e:
                    print("Exception occured")
                    r.remove(si)
                    ss.close()
                    break   
        self.stars()
'''