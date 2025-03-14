#基类应该尽量简单明了
import lxs,re,socket,threading

d = dict()
data = b''
datas =''
path = ""
paths = ''
ty = b'HTTP/1.1 200 ok\r\nContent-Type: '


def types(filename,paths):
    if(paths in d):
        return d[paths]
        pass
    else:
        lxs.Prx.url = 'https://e-hentai.org'+filename
        lxs.Prx.ipw = '104.20.135.21'
        l = lxs.Prx()
        l.pase()
        alls = l.sends()
        d[paths] = ty+b'text/html\r\n\r\n'+alls[1]
        return ty+b'text/html\r\n\r\n'+alls[1]
        pass


def formatting(value):
    value = value.decode()
    value = value.split(' ')[1]
    if(value=='/'):
        return ['/',value]
    else:
        z = value.split('/')
        print('z ',z)
        if(z[len(z)-1]==''):
            return [z[len(z)-2],value]
        else:
            return [z[len(z)-1],value]

def request(k,c):
    fg = formatting(k)
    path = fg[1]
    paths = fg[0]
    print(path)
    print(paths)
    zhi = types(path,paths)
    c.send(zhi)
    c.close()

    pass

def server(*a):
    def inits():
        d['ehg_index.c.js'] =ty+b'text/javascript\r\n\r\n'+ open('./server/ehg_index.c.js','rb').read()
        d['favicon.ico'] = ty+b'image/ico\r\n\r\n'+open('./server/favicon.ico','rb').read()
        d['ehg_gallery.c.js'] = ty+b'text/javascript\r\n\r\n'+open('./server/ehg_gallery.c.js','rb').read()
        d['ehg_show.c.js'] = ty+b'text/javascript\r\n\r\n'+open('./server/ehg_show.c.js','rb').read()
        d['g.css'] = ty+b'text/css\r\n\r\n'+open('./server/g.css','rb').read()
    inits()

    s = socket.socket()
    s.bind(a)
    s.listen()
    while True:
        con,ar = s.accept()
        print(con)
        sd= con.recv(1024)
        threading.Thread(target=request(sd,con)).start()
    pass

ti = threading.Thread(target=server('127.0.0.1',8000))
ti.start()
