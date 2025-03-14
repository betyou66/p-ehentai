import socket,lxs,os,asyncio,requests,re,aiohttp,aiofiles
#使用异步
#使用多线程的差别

async def writefile(file,data):
    async with aiofiles.open(file,mode='wb') as f:
        await f.write(data)

async def downloadimg(session,url):
    #ipb_session_id=8f2208f24aac08bc9572e004b15efdd5; 
    
    header1 = {'Connection':'keep-alive','Cookie':'ipb_member_id=4522602; ipb_pass_hash=a467850bb2d0fed80627d64931dcf99c; ipb_session_id=55875faddfd683a527ca68c2b7fc81ce; sk=bp8w6rdgmeci934fp919r6m7zp99;'}
    header2 = {'Connection':'keep-alive','Cookie':'ipb_member_id=7498513; ipb_pass_hash=e36bf990b97f805acb2dd5588440c203; sk=nf32h71b404ktqkgsgq2qgozdcfc;'}
    name = url.split('/')[-1]
    wjj = url.split('/')[-4]
    
    img = await session.get(url,ssl=False,headers=header1)
    data = await img.read()
    print(img.status)
    try:
        os.mkdir('./'+wjj)
    except:
        pass
    await writefile('./'+wjj+'/'+name,data=data)
    #with open('./'+wjj+'/'+name,'wb') as f:
    #    f.write(data)
    #    f.close()
    
    return str(url)        

async def request():
    with open('./fullimg.txt','rb') as d:
        j = d.read().decode('utf-8').split('"')
        url = [i for i in j if('https' in i)]
        #np = open('./fullimg.txt','wb')
        #np.write(b"")
        #np.close()
    session = aiohttp.ClientSession()

    tasks = [asyncio.create_task(downloadimg(session,img_url)) for img_url in url]
    #print(tasks)
    
    [await i async for i in asyncio.as_completed(tasks)]#:
    
   

    await session.close()



#delect 
        
asyncio.run(request())