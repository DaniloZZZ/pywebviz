import multiprocessing.dummy as thr

def threaded(f,*args):
    p = thr.Process(target=(f),args = args)
    p.start()
    return p
