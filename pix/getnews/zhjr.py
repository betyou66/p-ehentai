import asyncio,select,socket,requests,json,time,os,sys,ssl,http.server,re,json,urllib

class Main:
    __doc__ = """
    一个爬虫
        1. 查询消息
        2.yield迭代获取所需information
        2.1 爬取信息
              """
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.set_alpn_protocols(["http/1.1","spdy/2"])
    context.keylog_filename = "C:\dow\stable-diffusion-webui\一些小脚本\pix\key.log"
    #context.load_cert_chain(certfile="C:\dow\stable-diffusion-webui\一些小脚本\pix\zs\e.pem",keyfile="C:\dow\stable-diffusion-webui\一些小脚本\pix\zs\e.key")

    def __str__(self):
        return "hello world"
    def __init__(self) -> str:
        #https://cn.bing.com/translator?ref=TThis&text=%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3&from=&to=zh-Hans
        pass
'''
with socket.create_connection(("202.89.233.101",443)) as s:
    with Main.context.wrap_socket(s) as ss:
        ss.send(b"GET /translator?ref=TThis&text=%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3&from=&to=zh-Hans HTTP/1.1\r\nHost: cn.bing.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*\r\n\r\n")
        print(ss.recv(1024).decode())
'''
print("nǐhǎo")
print(1e-3)
