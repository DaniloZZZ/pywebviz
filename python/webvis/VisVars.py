from hosta import Hobject
import json
from . import interface as ifc

class VisVars(Hobject):
    name='VisVar'
    def serial(self):
        ser = {}
        for name, value in self.items():
            value, type_= ifc.preprocess_value(value)
            o = {'value': value, 'type': type_}
            ser[name] = o
        return json.dumps(ser)
