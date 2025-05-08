import aiohttp,asyncio,queue,pdb,threading,os
j = queue.Queue()
def indexs1(x):
    return x*9
import requests
def geturl(files)->list:
    with open(files,'rb') as w:
        end = w.read().decode().split('"')
        w.close()
    return [i for i in end if('https' in i)]
#print(geturl('./fullimg.txt'))
headers={'Connection':'keep-alive','Cookie':'ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; ipb_session_id=55875faddfd683a527ca68c2b7fc81ce; sk=bp8w6rdgmeci934fp919r6m7zp99;'}
def main(urls,paths):
    r = requests.get(urls,verify=False,headers=headers)
    with open(paths,'wb') as w:
        w.write(r.content)
        w.close()
    r.close()
#open('./cs.png','wb').write(r.content)
alls = geturl('./fullimg.txt')
try:
    os.mkdir('./'+alls[0].split('/')[-4])
except:
    pass
>>>>>>> 25eb782 (第6次提交)
for i in alls:
    path = './'+i.split('/')[-4]+'/'+i.split('/')[-1]
    #pdb.set_trace()
    try:
        print(path)
        t = threading.Thread(target=main,args=(i,path))
        t.start()
        t.join()

    except:
        pass

