
<div align="center">
    <img width="312px" alt="libvis logo" src="http://webvis.dev/logo.png"/>
</div>

This is a Image [libvis](http://libvis.dev) module

# Installation

`libvis-mods install gh:/libvis/Image`

# Usage

```python

from libvis.modules import Image
import numpy as np

vis.vars.image = Image(np.random.randn(200, 200))
vis.vars.nice_plot = Image.test_object()

```

