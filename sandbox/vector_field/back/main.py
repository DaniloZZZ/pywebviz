from libvis.modules import BaseModule

class vector_field(BaseModule):
    name="vector_field"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = """
vec2 get_velocity(vec2 p) {
  vec2 v = vec2(0., 0.);

  v.x = sin(sin(min(p.x/p.y,p.y)));
  v.y = .8*p.x;
  return v;
}
"""
        self.options = {
            'fade':.95,
            'count':7000,
            'color':'3'
        }

    def vis_get(self, key):
        value = self[key]
        print('sending value to front: ', key, value)
        return value

    def vis_set(self, key, value):
        super().vis_set(key, value) # same as self[key] = value
        print('updated value form front: ', key, value)

    @classmethod
    def test_object(cls):
        return cls()
