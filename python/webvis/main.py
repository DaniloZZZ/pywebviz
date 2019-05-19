import trio
import time

from VisWorker import Vis

def main():
    vis = Vis(
        ws_port=8000,
        vis_port=80
    )
    vis.show()

    N = [42, 12]
    vis.vars['test'] = N
    while True:
        N[1] += 1
        N[0] *= 2
        time.sleep(0.4)

if __name__=="__main__":
    main()
