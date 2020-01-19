from libvis.modules import BaseModule
import numpy as np
import json

class google_charts(BaseModule):
    name="google_charts"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = [['Foo', 'Bar','Baz']]
        self.data += [[i, np.sin(i/5), np.cos(i**2/20)]
                      for i in np.linspace(0, 20, 90)]
        self.title = 'React google charts'

    def vis_get(self, key):
        return self[key]

    @classmethod
    def test_object(cls):
        return cls()

