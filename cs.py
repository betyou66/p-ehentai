import asyncio,threading,socket,ssl,re,time
from multiprocessing import Process               
sj = time.time()
sz = open("./server/img/url.txt","rb").read()
lib = sz.decode().split("\r\n")
del lib[-1]


#异步网络下载io
#使用事件循环全部请求
#接受完数据才设置结果
#预处理，正在进行时，结束收尾时

#获得域名端口
#以下是cpu计算
def gethnpo(lj):
    z = lj.split("/")[2].split(":")
    name = z[0]
    port = z[1]
    path = lj.split(':')[2]
    wz = re.search('/',path)
    path = path[wz.span()[0]:]
    ip = socket.gethostbyname(name)
    return name,port,ip,path
#事件循环结束时
def data(d):
    give = d
    data = b''
    while True:
        dt = give[1].recv(4096)
        if(dt==b""):
            print('长度 ',len(data))
            break
        data += dt
    images = re.findall(b'\r\n\r\n(.*)',data, re.S)
    print('end')
    #print('耗时 :',time.time()-sj)
    open('./server/img/'+give[0],'wb').write(images[0])

#事件循环
task = []
lx = []

socket.setdefaulttimeout(10)
def cs(l):
    try:
        n,p,i,pa = gethnpo(l)
        print(pa)
        print(n)
        co = socket.create_connection((i,int(p)))
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        sco = context.wrap_socket(co,server_hostname=i)
        message = f'GET {pa} HTTP/1.1\r\nHost: {n}\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36\r\nAccept: image/*\r\n\r\n'
        sco.send(message.encode())
        lists = [pa.split('/')[-1],sco]
        print('set end\r\n',n)
        data(lists)
    except:
        print('error')
        pass
    
    
    #open("./server/img/url.txt","wb").write(b"")

#事件循环进行时
end = []

#对10个任务进行轮询读取
#多进程
for i in range(len(lib)):
    cs(lib[i])
print(time.time()-sj)
open("./server/img/url.txt","wb").write(b"")
