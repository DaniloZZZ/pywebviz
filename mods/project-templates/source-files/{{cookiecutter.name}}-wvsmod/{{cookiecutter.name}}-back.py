from webvis.models import BaseModule
import json

class {{cookiecutter.name}}:
    name={{cookiecutter.name}}
    def serial(self):
        json.dumps(self)
