from libvis.modules.Base import BaseModule
from .bottles import beer

class Bir(BaseModule):
    name="BirModule"
    def __init__(self):
        super().__init__()
        self.text = beer(3)

    def vis_set(self, key, value):
        super().vis_set(key, value) # same as self[key] = value
        if key=='count':
            try:
                rhymes = beer(int(value))
                self.text = rhymes
            except:
                pass
