from webvis.modules.Base import BaseModule

class TextModule(BaseModule):
    def __init__(self, val):
        super().__init__()
        self._val = val
        self.name = 'TextModule'

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._touch()
        self._val = val

    def ser(self):
        return {'val': self.val}


