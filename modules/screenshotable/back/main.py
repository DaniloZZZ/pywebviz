from libvis.modules import BaseModule
from libvis import interface as ifc
import time
import matplotlib.pyplot as plt

def plot_image(image, format='PNG'):
    import base64
    import io
    from matplotlib import pyplot as plt
    import matplotlib.image as mpimg

    i = base64.b64decode(image)
    i = io.BytesIO(i)
    i = mpimg.imread(i, format=format)

    plt.imshow(i, interpolation='nearest')
    plt.show()

class screenshotable(BaseModule):
    name="screenshotable"
    def __init__(self, object):
        super().__init__(object=object)

    def vis_get(self, key):
        #value = super().vis_get(key) # makes {value:preprocess(value), type:self.name}
        value = super().vis_get(key) # makes {value:preprocess(value), type:self.name}
        value = ifc.serialize_to_vis(value)
        return value

    def vis_set(self, key, value):
        super().vis_set(key, value) # same as self[key] = value
        print('updated value form front: ', key, value)
        if key=='trigger':
            self.show()

    def show(self):
        if 'image' in self.keys():
            image = self.image
        else:
            self.get_image = True
            image = None
            for _ in range(10):
                time.sleep(0.5)
                print(self)
                if 'image' in self.keys():
                    print('got image!', self.image)
                    image = self.image

        if image is None:
            print("Didn't receive image, try sending it from front.")
            return
        plot_image(image.split('base64,')[1])


    @classmethod
    def test_object(cls):
        return cls(object=[1,3,4,3.3,5])
