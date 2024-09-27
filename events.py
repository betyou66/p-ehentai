import os,re,threading,asyncio,ssl,socket
import contextvars
loop = asyncio.new_event_loop()

path = '/'
#TLS加密
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False
context.keylog_filename = './key.log'


class Ehen(asyncio.Protocol):
    def connection_made(self,transport):
        self.transport = transport
        pass
    def setpath(self,d):
        self.path = d
    def data_received(self,data):
        self.transport.write(b"GET "+self.path.encode("utf-8")+b" HTTP/1.1\r\nHost: e-hentai.org\r\nUser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nConnection: keep-alive\r\n\r\n")
        #await asyncio.sleep(3)
        print(data[0:100])
        return data


async def end(m):
    await connect()
    m.set_result('123')

async def connect():
    global path

    c = await loop.create_connection(Ehen,ssl=context,host='104.20.135.21',port=443)
    print(c)
    c[1].setpath('/')
    print(c[1].data_received(1))
    await asyncio.sleep(3)
    print(c[1].data_received(1))
    c[1].close()

fp = loop.create_future()

taskpool = []
taskpool.append(loop.create_task(end(fp)))
loop.run_until_complete(*taskpool)
