import socket
import ssl
import asyncio
import threading
import select
import os
import io
import time

#ip="210.140.92.187"

async def ma():#异步入口
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    #要求对方发送证书
    context.check_hostname = False
    #不验证主机名
    context.set_alpn_protocols(["http/1.1","spdy/2"])
    #告诉对方协议
    context.keylog_filename = "C:\dow\stable-diffusion-webui\一些小脚本\pix\key.log"
    #context.sni_callback = sni_callback(client_connection=ssl.SSLContext, server_name=None, ssl_context=context) 
    # #print(ssl.get_server_certificate((ip,prot)))
    async def main(hostname,ip,port,defa):#通过ip建立连接然后用ssl包裹加密通话
        try:
            print(hostname)
            if not ip:
                ip="127.0.0.1"
            if not port:
                port=443
            #print(ssl.get_server_certificate((ip,port)))
            print(ip)
            ipaddr=socket.gethostbyname_ex(hostname)[2]
            print(ipaddr)
            if not ipaddr[1]:
                ip=ipaddr[0]
            else:
                ip=ipaddr[1]
            print(ip)
           # print(socket.gethostbyaddr(hostname))
        except:
            pass
        with socket.create_connection((ip, port)) as sock:
            with context.wrap_socket(sock, server_hostname=ip) as ssock:
                ssock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,8**10)

                defa.send(b"HTTP/1.1 HTTP 200 Connection Established\r\n\r\n")
                #ssock.sendall(b"GET / HTTP/1.1\r\nHost: "+hostname.encode("utf-8")+b"\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nConnection: keep-alive\r\nCookie: BIDUPSID=89ABF44FF34972088E2D12CBE8866D6B; PSTM=1699298111; BAIDUID=89ABF44FF34972088E2D12CBE8866D6B:FG=1; ZFY=OfupELOn8CjdrVelvr2lX86qqXx7tsIKOU8l0hWW558:C; COOKIE_SESSION=0_0_1_1_0_0_1_0_1_0_0_0_0_0_0_0_0_0_1699318986%7C1%230_0_1699318986%7C1; H_PS_PSSID=39712_39780_39789_39787_39704_39795_39683_39661_39678_39839_39903_39819_39909; BD_UPN=13314752\r\nUpgrade-Insecure-Requests: 1\r\n\r\n")
                datasi=b""
                timeout=0

                while True:
                    try:   
                        timeout+=1
                        #print(defa.recv(1024))
                        ssock.send(defa.recv(1024))
                        defa.send(ssock.recv(1024))
                        if timeout>5:
                            ssock.close()
                            print("结束")
                            break

                    except:
                        pass
    '''
#获取证书给客户端
    async def ca(cs,ae):
        ipad = socket.gethostbyname_ex(cs)[2]
        try:
            zshu = ssl.get_server_certificate((ipad[0],ae))
        except:
            zshu = ssl.get_server_certificate((ipad[1],ae))
        print(zshu)
        open("C:\dow\stable-diffusion-webui\一些小脚本\pix\e.cer","w").write(zshu)
        return True

#检查文件发生变化发送给客户端
    async def sends(c,a):
        c.sendto(b"HTTP/1.1 200 Connection Established\r\nFiddlerGateway: Direct\r\nClientToServerBytes: 1416\r\nServerToClientBytes: 1358\r\n\r\n",a)
        print(c)
        print(c.recv(1024))
        c.sendto(open("C:\dow\stable-diffusion-webui\一些小脚本\pix\e.cer","r").read().encode("utf-8"),a)
        sz = open("C:\dow\stable-diffusion-webui\一些小脚本\worker-delicate-truth-06a8\li.html","rb").read()
        c.sendto(sz,a)
        c.sendto(b"Connection: close\r\n\r\n")
        c.close()
        '''
    async def https_proxyserver():#套接字本地代理服务器
        try:
            server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1",8081))
            server.listen(1)
            while True:
                client,addr = server.accept()
                data = client.recv(1024)
                datas = data.splitlines()
                print(datas)
                print(datas[0].decode("utf-8").replace(" ",",").splitlines())
                print(datas[0].decode("utf-8").replace(" ",",").splitlines()[0].split(","))
                up = datas[0].decode("utf-8").replace(" ",",").splitlines()[0].split(",")[1].split(":")
                print(socket.gethostbyname(up[0])," ip")
                print(up[1]," 端口")
                print(up[0]," 域名")
                await asyncio.gather(main(up[0],None,up[1],client))
        except:
            pass

    await https_proxyserver()

#asyncio.run(https_proxyserver())
asyncio.run(ma())

