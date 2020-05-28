from libvis.modules.Base import BaseModule
from .bottles import beer

class Bir(BaseModule):
    name="BirModule"
    def __init__(self):
        super().__init__()
        self.count = 7
        self.text = beer(self.count)

    def vis_set(self, key, value):
        super().vis_set(key, value) 
        try:
            rhymes = beer(int(value))
            self.text = rhymes
            self.count = int(value)
        except:
            self.count = 0

    def vis_get(self,name):
        return self[name]

