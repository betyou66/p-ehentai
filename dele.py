
import os,re,zipfile,cs
pat = './server/img/'
loop = False
for i in os.listdir('./server/img'):
    if(re.search('.jpg',i)!=None):
        szhi = 100
        if(loop==False):
            for ig in range(szhi):
                if(f"img{ig}.zip" in os.listdir('./server/img')):
                    print('已存在')
                else:
                    filename = f'img{ig}.zip'
                    loop = True
                    zi = zipfile.ZipFile('./server/img/'+filename,'x')
                    break
        zi.write(pat+i)

for i in os.listdir('./server/img'):
    if(re.search('.jpg',i)!=None):
        os.remove('./server/img/'+i)

