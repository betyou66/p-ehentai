import bs4,thrdli,re,time,asyncio,threading,queue,random,threading,concurrent.futures,requests

#markups = '<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n<meta charset="utf-8" />\r\n<link rel="stylesheet" type="text/css" href="https://127.0.0.1:8000/g.css" /></head><body>\r\n<script type="text/javascript">\r\nfunction popUp(URL,w,h) {window.open(URL,"_pu"+(Math.random()+"").replace(/0\./,""),"toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width="+w+",height="+h+",left="+((screen.width-w)/2)+",top="+((screen.height-h)/2));return false;}\r\n</script>\r\n</body>\r\n</html>'
markups = '<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n<script>\r\n\r\nfunction load() {\r\nvar xhl =new XMLHttpRequest();\r\nxhl.open("GET","http://127.0.0.1:8000/cs",true);\r\nxhl.send();\r\nxhl.onreadystatechange = function() {\r\nconsole.log(xhl.response)\r\ndocument.body.innerHTML = xhl.response\r\n}\r\n\r\n}\r\nwindow.setInterval(load,20000);\r\n</script>\r\n<meta charset="utf-8" />\r\n<link rel="stylesheet" type="text/css" href="http://127.0.0.1:8000/g.css" />\r\n</head>\r\n<body>\r\n</body>\r\n</html>'
#<script>\r\n\r\nfunction load() {\r\nvar xhl =new XMLHttpRequest();\r\nxhl.open("GET","http://127.0.0.1:8000/cs",true);\r\nxhl.send();\r\nconsole.log(xhl.response);\r\nxhl.onreadystatechange = function() {\r\ndocument.body.innerHTML = xhl.response\r\n}\r\n\r\n}\r\nwindow.setInterval(load,1000);\r\n</script>
#.format(lj='https://127.0.0.1:8000/'+1+sta.query+sta.types)
#gj.insert(5,'<script>const socket = new WebSocket("ws://127.0.0.1:8001");\r\nsocket.addEventListener("message", function (event) {\r\nasync function cs(blob){\r\nconst text = await new Response(blob).text();\r\ndocument.body.innerHTML = text;\r\n}\r\ncs(event.data)});\r\nfunction se(){\r\nsocket.send("'+paths[11:]+'")};\r\nwindow.setInterval(func=se,6000)\r\n</script>')
'''
i = i.replace(i[re.search('onerror',i).span(0)[0]:re.search('src',i).span(0)[0]],'')
'''
#=自构造网页
#根据起始网页获得结束网页数量



def getstartatend(path=None,dat=None,m=markups)->list:
        '''
    param path:起始网页路径
    param m:自构造网页
    return [t,m]:[结束网页数量,添加了标题的自构造网页]
    param dowhtnl 第二页
    '''
        starts = 0
        if path!=None:
            soup = bs4.BeautifulSoup(open(path,"rb").read(),"html.parser")
        elif dat!=None:
            soup = bs4.BeautifulSoup(dat,"html.parser")
        try:
            span = soup.find_all('span')
            t = ''
            for i in range(len(span)):
                if(t==''):
                    t = int(span[i].string)
                    starts = t
                elif t<int(span[i].string):
                    t = int(span[i].string)
            #t是有多少页
        except:
            pass
        title = soup.find_all('title')
        #print(soup)
        htmlsl = m.split('\r\n')
        for i in range(len(htmlsl)):
            if(htmlsl[i].find('title')==-1):
                #print(title[-1])
                htmlsl.insert(i,str(title[-1]))
                break
        onck = soup.find_all('a',id='next')
        dowhtnl = ''
        for i in onck: 
            dowhtnl = i['href']
            #print(dowhtnl)
        img = ''
        img = str(soup.find_all('img',id='img'))
        #print("src: ",soup.find_all('img',id='img').src)
        try:
            if(img[7]=='='):
                img = ''.join(img.split(img[6:10]))
                img = img[1:-1]
            else:
                if(img[-1]=='>'):
                    img = ''.join(img[0:-1])
                    img = img[1:-1]
                else:
                    img = ''.join(img[0:-1])+'>'
                    img = img[1:-1]
            return [starts,t,dowhtnl,img]
        except:
            if(img[-1]=='>'):
                img = ''.join(img[0:-1])
                img = img[1:-1]
            else:
                img = ''.join(img[0:-1])+'>'
                img = img[1:-1]
            return [starts,t,dowhtnl,img]
#全局变量
dowhl = 0#
tp = []#图片数据
tarage = []#目标页面
starthtl = b''#更新数据
end = [0]#结束
image = ''
look = threading.Lock()#线程锁
hec = markups.split('\r\n')#保存的文件
alldata = []
stat = False
'''
都需要更新
image,starthl,dowhl
'''
def getall():
    global tp,dowhl,tarage,starthtl,image,end,alldata,stat
    end[-1] -= 1

    if('https://127.0.0.1:8000/'):
        thrdli.Prx.url = 'https://e-hentai.org/'+dowhl[22:]
    else:
        thrdli.Prx.url = 'https://e-hentai.org'+dowhl[20:]
        
    open('./server/url.txt',"ab").write(thrdli.Prx.url.encode('utf-8')+b'\r\n')
    open("./server/img/url.txt","ab").write(image.split('"')[3].encode("utf-8")+b"\r\n")
    print(image.split('"')[3].split("/")[-1])
    
    shi = thrdli.Prx()
    shi.pase()
    file,dp = shi.sends()
    tp.append(image)
    #对下一页数据处理
    starthtl = dp
    s,t,d,i = getstartatend(dat=starthtl)
    dowhl = d
    image = i
    #print(image)
    hec.insert(-2,i)
    dsp = '\r\n'.join(hec).encode('utf-8')
    open('./server/cs.html','wb').write(dsp)
    print('look ', end)
    if(end[0]==0):
        stat = False
        del tarage[0]
        img = open("./server/img/url.txt","rb").read()
        img1 = img.decode("utf-8").split("\r\n")
        
        print('下载完成')
    look.release()

open("./server/img/url.txt","w").write('')
#getall(d=open('C:\dow\stable-diffusion-webui\一些小脚本\pix\server/2795250-1.html','rb').read())


'''
async def returnfuture(hs,ar): #测试新建线程
        loop=asyncio.get_event_loop() 
        newexecutor=concurrent.futures.ThreadPoolExecutor()
        print(ar," 异步里的参数")
        try:
            future=await loop.run_in_executor(newexecutor,hs(ar))#执行阻塞函数
        except:
            pass
        #print(future)
'''
#主入口
        


def main(*args):
    global alldata,stat
    if(''.join(args) in alldata):
        pass
    else:
        alldata.append(''.join(args))
    #print(alldata)
    def csh(argsi):
        global dowhl,tarage,starthtl,image,hec,alldata,end,stat
        stat = True
        starthtl = argsi
        #初始化数据
        s,t,ds,i = getstartatend(dat=starthtl)
        t = t-s
        end[0] = t
        hec.insert(-2,i)
        tp.append(i)
        tarage.append(t)#要创建的多少线程
        threadpool = []
        dowhl = ds#下一页
        image = i
        for i in range(tarage[-1]):
            threadpool.append(threading.Thread(target=getall))
        for i in range(len(threadpool)):
            look.acquire()
            threadpool[i].start()
        print(end,"  end")
       #重置全局变量

    if(stat==False):
        mulit = threading.Thread(csh(alldata[-1]))
        mulit.start()
    while True:
            if(stat==False):
                print('重置了')
                if(len(alldata)!=0):
                    del alldata[0]
                for i in range(len(alldata)):
                    try:
                        print(len(alldata),' alldata len')
                        csh(alldata[0])
                        del alldata[0]
                    except:
                        stat = True
                        pass
                break
            time.sleep(1)
