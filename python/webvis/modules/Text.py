from webvis.modules.Base import BaseModule

class TextModule(BaseModule):
    def __init__(self, val):
        super().__init__()
        self.val = val

    @property
    def val(self):
        return self.val

    @val.setter
    def set_val(self, val):
        self._touch()
        self.val = val

    def ser(self):
        return {'val': self.val}


