import threading
import multiprocessing as m
import time
sj = time.time()
def mainwork():
    for i in range(5):
        print(i)
    print(f'start: {sj}','end: '+str(time.time()))
jc = m.Process(target=mainwork)

jc.start()

