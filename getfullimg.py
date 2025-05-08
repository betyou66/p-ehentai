'''
使用异步

id=next
'''
img = set()
allurl = dict()

url = input()
print(url)
shual = 0
import asyncio,re,aiohttp,random,requests,threading
async def downhtml(session):
    global allurl,url,shual
    header = {'Connection':'keep-alive'}
    request = await session.get(url,ssl=False,headers=header)
    data = await request.read()
    status = request.status
    proxy = '"https://cs.sduoi.top/'
    try:
        full = re.search(r'(?<=e-hentai.org)/fullimg(.*?)"',data.decode()).group(0)
        img.add('"https://e-hentai.org'+full+'\r\n')
        #img.add(proxy+'https://e-hentai.org'+full+'\r\n')
        next = re.search(r'(<a id="next")(.*?)>',data.decode()).group(0).split(' ')[-1].split('=')[-1].split('>')[0].split('"')[1]
        shual = int(re.findall(r"(<span>(.*?)</span>)",data.decode())[1][1])-1
        #allurl = {i:"" for i in range(int(shual))}
        #allurl[0] = {url:status}
        #allurl[1] = next
        allurl.update({url:status})
        url = next

        return full,next
    except:
        next = re.search(r'(<a id="next")(.*?)>',data.decode()).group(0).split(' ')[-1].split('=')[-1].split('>')[0].split('"')[1]
        shual = int(re.findall(r"(<span>(.*?)</span>)",data.decode())[1][1])-1
        #allurl = {i:"" for i in range(int(shual))}
        #allurl[0] = {url:status}
        #allurl[1] = next
        allurl.update({url:status})
        url = next
        full = False

        return full,next
        pass
async def main():
    global shual
    session = aiohttp.ClientSession()
    i,u = await downhtml(session)

    for i in range(shual):
        i,u = await downhtml(session)
    await session.close()
    with open('./fullimg.txt','wb') as x:
        for i in img:
            x.write(i.encode())
        x.close()

        pass
    #await fullimg1.request()
asyncio.run(main())
