from webvis.modules import BaseModule
import json

class {{cookiecutter.name}}(BaseModule):
    name="{{cookiecutter.name}}"
    def serial(self):
        return json.dumps(self)
