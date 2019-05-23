import json
#from . import helpers as h
try:
    import matplotlib
    import mpld3
    import bokeh
except Exception as e:
    print(e)

def is_mpl(val):
    try:
        return isinstance(val, matplotlib.figure.Figure)
    except Exception as e:
        return False
def is_bokeh(val):
    try:
        return isinstance(val,bokeh.model.Model) or isinstance(val,bokeh.document.document.Document)
    except Exception as e:
        return False

def get_var(val, params):
    """
    Val: some value from user
    params: dict of params from frontend
    """
    if is_bokeh(val):
        ret = bokeh.embed.file_html(val, bokeh.resources.Resources('cdn'))
        type_ = 'mpl'
    elif is_mpl(val):
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
