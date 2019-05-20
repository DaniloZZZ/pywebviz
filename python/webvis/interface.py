import json
#from . import helpers as h
import matplotlib
import mpld3
import bokeh

def get_var(val, params):
    """
    Val: some value from user
    params: dict of params from frontend
    """
    if isinstance(val,bokeh.model.Model) or isinstance(val,bokeh.document.document.Document):
        ret = bokeh.embed.file_html(val, bokeh.resources.Resources('cdn'))
        type_ = 'mpl'
    elif type(val)==matplotlib.figure.Figure:
        ret = mpld3.fig_to_html(val)
        type_ = 'mpl'
    else:
        ret = val
        type_ = 'raw'

    msg = {'args':params['varname'],
           'value':ret,
           'type':type_
          }
    return json.dumps(msg)
