from webvis.modules import BaseModule
from webvis.modules import BaseTestModule
import torch as tch

class torch(BaseModule):
    name="torch"
    def __init__(self, tensor):
        super().__init__()
        self.tensor = tensor

    def vis_get(self, name):
        return self.tensor.tolist()

    @classmethod
    def test_object(cls):
        return cls(tch.ones((20,30)))

class test_torch(torch, BaseTestModule):
    @classmethod
    def test_object(cls):
        return cls(tch.ones((2,3)))
