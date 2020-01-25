from libvis.modules import BaseModule

class latex(BaseModule):
    name="latex"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tex = " e^{i\pi} = -1"

    def vis_get(self, key):
        return self[key]

    @classmethod
    def test_object(cls):
        return cls()

