class BaseModule:
    def __init__(self):
        self._touched = True

    def _touch(self):
        self._touched = True

    def ser(self):
        return self.__dict__



