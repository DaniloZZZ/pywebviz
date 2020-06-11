
from libvis.modules import BaseModule
import json
from .utils import random_quote

class Button(BaseModule):
    name="uicontrols"
    def __init__(self,label='My Button', on_press=print):
        super().__init__(label=label, on_press=on_press)
        self.depressed = False

    def vis_set(self, key, value):
        if key == 'depressed':
            if self.depressed:
                if value is False:
                    self.on_press()
        self.depressed = value

    def vis_get(self, key):
        if key == 'on_press':
            return 'function'
        return self[key]


def test_object():
    button =  Button(on_press=print)
    def on_press():
        button.label = button.label[::-1]
    button.on_press = on_press
    return button
