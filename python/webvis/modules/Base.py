from hosta import Hobject

class BaseModule(Hobject):
    def _touch(self):
        self._touched = True

    def serial(self):
        return self.__dict__



