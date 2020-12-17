import multiprocessing
def process(index):
    print(f'Process:{index}')
if __name__=='__main__':
    for i in range(10000):
        p=multiprocessing.Process(target=process,args=(i,))
        p.start()
#如果说你是海上的烟火我就是试着玩一把大的好吧