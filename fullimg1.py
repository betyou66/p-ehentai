import os,asyncio,queue,pdb,full,random,requests,threading
#使用异步
#使用多线程的差别

def downloadimg(url,name,dirs):
    header1 = {'Connection':'keep-alive','Cookie':'ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; ipb_session_id=55875faddfd683a527ca68c2b7fc81ce; sk=bp8w6rdgmeci934fp919r6m7zp99;'}
    header2 = {'Connection':'keep-alive','Cookie':'ipb_member_id=7498513; ipb_pass_hash=e36bf990b97f805acb2dd5588440c203; sk=nf32h71b404ktqkgsgq2qgozdcfc;'}
    name = name
    wjj = dirs

    try:
        img = requests.get(url,verify=False)
        try:
            os.mkdir('./'+wjj)
        except:
            pass
        with open(f'./{wjj}/{name}','wb') as w:
            w.write(img.content)
            w.close()

    except Exception as e:
        print(img)
        #pdb.set_trace()
        #breakpoint()
        print(e)
    finally:
        print(img.status_code)

async def request():
    with open('./fullimg.txt','rb') as d:
        j = d.read().decode('utf-8').split('"')
        url = [i for i in j if('https' in i)]
    Trueimage = []
    import time
    try:
        for i in url:
            fa = full.Prx(i,'104.20.19.168',{})
            fa.pase()
            names,urls,dirs = fa.sends()
            task = threading.Thread(target=downloadimg,args=(urls,names,dirs,))
            task.start()

            print(urls,dirs)
    except Exception as e:
        print(e)
    finally:
        with open('./fullimg.txt','wb') as w:
            w.write(b'')
            w.close()



asyncio.run(request())
