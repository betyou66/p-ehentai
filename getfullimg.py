'''
使用异步

id=next
'''
img = ''
allurl = dict()

url = input()
shual = 0
import asyncio,re,aiohttp,random,requests,threading
def downhtml():
    global allurl,url,shual,img
    header = {'Connection':'keep-alive'}
    request = requests.get(url,verify='/home/kali/nginx/ca.crt',headers=header)
    data = request.text
    status = request.status_code
    proxy = 'https://cs.sduoi.top/'
    try:
        full = re.search(r'(?<=e-hentai.org)/fullimg(.*?)"',data).group(0)
        img = 'https://e-hentai.org'+full.split('"')[0]
        next = re.search(r'(<a id="next")(.*?)>',data).group(0).split(' ')[-1].split('=')[-1].split('>')[0].split('"')[1]
        shual = int(re.findall(r"(<span>(.*?)</span>)",data)[1][1])-1
        allurl.update({url:status})
        if(next==url):
            raise ValueError('重复')
        url = next

        return full,next
    except:
        next = re.search(r'(<a id="next")(.*?)>',data).group(0).split(' ')[-1].split('=')[-1].split('>')[0].split('"')[1]
        shual = int(re.findall(r"(<span>(.*?)</span>)",data)[1][1])-1
        allurl.update({url:status})
        if(next==url):
            raise ValueError('重复')
        url = next
        full = False

        return full,next
        pass
    finally:
        request.close()
def main():
    global shual,img
    i,u = downhtml()
    yield img
    for i in range(shual):
        i,u = downhtml()
        yield img
    #with open('./fullimg.txt','ab') as x:
    #    for i in img:
    #        x.write(i.encode())
    #    x.close()
#c = main()
#for i in c:
#    print(i)
#    breakpoint()
