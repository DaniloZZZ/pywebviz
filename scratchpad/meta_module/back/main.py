""" Example of how to write meta modules in libvis:
    modules that wrap another modules
"""
from libvis import VisVars

class meta_module(VisVars): #pylint: disable=invalid-name, too-many-ancestors
    """
    A libvis module that takes a module in attribute
    `submod` and displays it in a frame
    """

    name = "meta_module"

    def vis_set(self, key, value):
        super().vis_set(key, value) # same as self[key] = value
        print('updated value form front: ', key, value)

    @classmethod
    def test_object(cls):
        module = cls()
        from libvis.modules import google_charts
        module.len = 20
        module.list = list(range(module.len))
        module.chart = google_charts.test_object()
        return module
