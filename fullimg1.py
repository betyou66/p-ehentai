import os,asyncio,queue,pdb,full,random,requests,threading,getfullimg
#使用异步
#使用多线程的差别

def downloadimg(url,name,dirs):
    header1 = {'Connection':'keep-alive','Cookie':'ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; ipb_session_id=55875faddfd683a527ca68c2b7fc81ce; sk=bp8w6rdgmeci934fp919r6m7zp99;'}
    header2 = {'Connection':'keep-alive','Cookie':'ipb_member_id=7498513; ipb_pass_hash=e36bf990b97f805acb2dd5588440c203; sk=nf32h71b404ktqkgsgq2qgozdcfc;'}
    name = name
    wjj = dirs

    try:
        img = requests.get(url)
        try:
            os.mkdir('../ehimg/'+wjj)
        except:
            pass
        with open(f'../ehimg/{wjj}/{name}','wb') as w:
            w.write(img.content)
            w.close()

    except Exception as e:
        print(e)
    finally:
        print('close')
        try:
            img.close()
        except:
            pass
        pass
        #print(img.status_code)

def request():
    #with open('./fullimg.txt','rb') as d:
    #    j = d.read().decode('utf-8').split('"')
    #    url = [i for i in j if('https' in i)]
    #Trueimage = []
    try:
        startimg = getfullimg.main()

        for i in startimg:
            print(i)
            #breakpoint()
            fa = full.Prx(i,'104.20.19.168',{})
            fa.pase()
            names,urls,dirs = fa.sends()
            #breakpoint()
            print(names,urls,dirs)
            task = threading.Thread(target=downloadimg,args=(urls,names,dirs,))
            task.start()
            #time.sleep(random.randint(3,5))
            #print(urls,dirs)
    except Exception as e:
        task.join()
        print(e)
    finally:
        print('执行完毕 %s' % urls)
        #with open('./fullimg.txt','wb') as w:
        #    w.write(b'')
        #    w.close()



request()
