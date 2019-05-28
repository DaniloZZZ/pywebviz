import json
import numpy as np
#from . import helpers as h
import matplotlib
import mpld3
from bokeh.model import Model as bModel
from bokeh.document.document import Document as bDocument
import bokeh


def get_var(val, params):
    """
    Val: some value from user
    params: dict of params from frontend
    """
    if isinstance(val,bModel) or isinstance(val,bDocument):
        ret = bokeh.embed.file_html(val, bokeh.resources.Resources('cdn'))
        type_ = 'mpl'
    elif type(val)==matplotlib.figure.Figure:
        ret = mpld3.fig_to_html(val)
        type_ = 'mpl'
    elif type(val)==np.ndarray:
        sh = val.shape
        if len(sh) >= 2:
            if sh[0]>10 and sh[1]>10:
                alpha = np.ones(list(sh[:2])+[1])*255
                if len(sh)==2:
                    val = val.reshape(sh[0],-1,1)
                    val = np.concatenate((val,val,val,alpha),axis = -1)
                if len(sh)==3:
                    val = np.concatenate((val,alpha), axis=-1)
                val = val.flatten()
                ret = list(sh[:2]) + val.tolist()
                type_='img'

        else:
            val = val.tolist()
            ret = val
            type_ = 'raw'
    else:
        ret = val
        type_ = 'raw'

    msg = {'args':params['varname'],
           'value':ret,
           'type':type_
          }
    return json.dumps(msg)
