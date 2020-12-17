import threading
import time
def target(second):
    print(f'Theading{threading.current_thread().name}is running')
    print(f'Theading{threading.current_thread().name}sleep {second}s')
    time.sleep(second)
    print(f'Theading{threading.current_thread().name}is ended')
print(f'Theading{threading.current_thread().name}is running')
for i in [1,5]:
    t=threading.Thread(target=target,args=[i])
    t.start()
print(f'Theading{threading.current_thread().name}is ended')
#世上本没有路走的人多了就成了路了呀