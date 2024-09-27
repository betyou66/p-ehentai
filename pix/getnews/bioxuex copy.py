from bs4 import BeautifulSoup
import re
import asyncio
sz = open('C:\dow\stable-diffusion-webui\一些小脚本\pix\server/2792623-1.html','rb').read()
jie = BeautifulSoup(sz,'html.parser')
script = jie.find_all('script')
img = jie.find_all(id='img')[0]
span = jie.find_all('span')
t = ''
for i in range(len(span)):
    if(t==''):
        t = int(span[i].string)
    elif t<int(span[i].string):
        t = int(span[i].string)

cs = str(img)
print(''.join(cs.split(cs[5:9])))
print(int(5))
print(t)