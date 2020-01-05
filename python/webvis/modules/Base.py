from webvis import VisVars

class BaseModule(VisVars):
    def _touch(self):
        self._touched = True

    def serial(self):
        return self.__dict__



