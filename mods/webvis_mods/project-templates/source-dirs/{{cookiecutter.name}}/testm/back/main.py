from webvis.modules import BaseModule
import json
from .utils import random_quote

class testm(BaseModule):
    name="testm"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quote = random_quote()

    def serial(self):
        return json.dumps(self)
