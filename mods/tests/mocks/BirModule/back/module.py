from libvis.modules.Base import BaseModule
from .bottles import beer

class Bir(BaseModule):
    name="BirModule"
    def serial(self):
        try:
            cnt = int(self.count)
        except:
            cnt = 5
        rhymes = beer(cnt)
        return rhymes
