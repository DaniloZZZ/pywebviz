from libvis.modules import BaseModule


def test_object():
    class MyType:
        value = 1

    return MyType()

def to_type_and_dict(mytype):

    return 'func', {'value': 'mytype.value'}

name = 'func'
