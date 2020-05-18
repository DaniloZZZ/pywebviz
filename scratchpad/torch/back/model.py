import torch

from libvis.modules import BaseModule
from libvis.modules import BaseTestModule
from .tensor import Tensor
from .test_model import Net

def named_params2tensor_dict(params):
    return {
        name: param.data for name, param in params
    }

class Model(BaseModule):
    name='torchTensor'
    def __init__(self, model):
        super().__init__()
        named_params = list(model.named_parameters())

        params  = [[name, Tensor(param.data)] for name, param in named_params]

        self.model = params[-4:]

def test_object():
    model = Net()
    return Model(model)
