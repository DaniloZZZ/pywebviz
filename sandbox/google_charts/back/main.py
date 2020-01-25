from libvis.modules import BaseModule
from .bubble import BubbleChart
import numpy as np

class AreaChart(BaseModule):
    name="google_charts"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = [['X', 'Bar','Baz']]
        self.data += [[i, np.sin(i/5), np.cos(i**2/20)]
                      for i in np.linspace(0, 20, 90)]
        self.title = 'React google charts'
        self.hAxis = 'X'
        self.type = 'AreaChart'

    def vis_get(self, key):
        return self[key]

def test_object():
    return BubbleChart()
