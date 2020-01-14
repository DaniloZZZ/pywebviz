from webvis.modules import BaseModule
from webvis.modules import BaseTestModule
import torch

class Tensor(BaseModule):
    name="torchTensor"
    def __init__(self, tensor):
        super().__init__()
        self.tensor = tensor

    def vis_get(self, name):
        return self.tensor.tolist()

class test_torchTensor(Tensor, BaseTestModule):
    @classmethod
    def test_object(cls):
        return cls(torch.rand(30,30))
