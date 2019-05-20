import multiprocessing.dummy as thr
import mpld3
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def threaded(f,*args):
    p = thr.Process(target=(f),args = args)
    p.start()
    return p

def get_mpl_html(value, config=None):
    fig, ax = plt.subplots()
    try:
        ax.plot( value )
    except Exception as e:
        return str(e)
    s = mpld3.fig_to_html(fig)
    plt.close(fig)
    return s


