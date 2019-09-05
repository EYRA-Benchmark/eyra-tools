Building these docs
-------------------

:ref:`Install the EYRA Tools package<installation:Installation>`.

Run ``make html`` from the ``docs/`` folder. This will generate an html
version of the documentation in ``docs/_build/html``.

.. code-block:: bash

    # Build docs to docs/_build/html
    cd docs
    make html

The EYRA Iris Demo scripts have to be copied to ``docs/code/demo`` by hand.
You only have to do this if scripts from `the demo
<https://github.com/EYRA-Benchmark/eyra-iris-demo>`_ are updated.
