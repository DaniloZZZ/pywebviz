Quick start
===========

First steps
-----------

Fire up your ``python`` interpreter or jupyter notebook
and type the following:

::
   from webvis import Vis

   vis = Vis()
   vis.start()
   vis.vars.test = [ x**2 for x in range(-20,20) ]

Now, open `localhost:7700 <localhost:7700>` in your browser.

There's not much there now, 
but let's go ahead and click 'Add Widget' button at the top left.


Widgets are basic blocks of our dashboard, you can drag them and resize.

type in the name of your variable, ``test``, and your array will appear.

.. image:: pictures/quickstart.png
   :alt: Dashboard with y=x^2 graph

Interactive
-----------

Now, the most awesome feature about libvis is that
python objects form ``vis.vars`` are automatically synchronized.


Try this one:
::
   v.vars.test += [20**2]*5

Any time you assign to an attribute of ``Vis.vars``, stores it in a 
special place, and another thread that listens to updates sends data 
to the app via websocket.

