
.. image:: https://img.shields.io/pypi/v/webvis.svg
    :target: https://pypi.python.org/pypi/webvis
    :alt: PyPi version


Data visualization made easier
==============================

This is a project for interactive data visualization

It uses a dedicated web app with cards that display python variables.

Check out the notebooks folder for examples

Jump right in: `Quick start <http://docs.webvis.dev/usage/quickstart.html#>`_.


Quick start
-----------

.. code-block:: python

   from webvis import Vis

   vis = Vis(vis_port=7007)

   vis.vars.test = "Hello World!"

   # Open the browser on 7007 port 
   vis.show()


Then change the name in card to "test", and your variable will appear!

The values are updated dynamically, a separate thread is created that checks the changes.

values can be matplotlib figures, 1-d and 2-d arrays,
and even bokeh is supported!


Simple Feature list
-------------------

Usecase: machine learning

- Watch **and change** learning rate
- Watch Loss and accuracy
- Watch output pictures on prediction
- Display confusion matrix
- Control experiments using simple buttons

Advanced: 

- Download data of widget
- Filter data to download and send

Feedback from ODS:

- Graph val accuracy vs train accuracy:
  solved with custom X axis.
- Fast pictures:
  Solved using legimens module with dict of pictures
- Native support for confusion matrix:
  Solved by bokeh/matplotlib. 
- Storing format of data: Solved by caching utility in front.
  Also solvable by hook in legimens send
- Control experiments in browser: Solved by
  button and lock controls.
- Filter data: For God's sake use `grep`. But what if need to filter by 'greater than'?
- Criteria for outliers: Solved by returning nothing in serializer.
- Large files: Use a dedicated trio coro for every object.
