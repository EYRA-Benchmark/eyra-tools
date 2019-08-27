Installation
------------

Requirements
############

Make sure you have the following tools installed:

- Docker
- Python 3.5+
- virtualenv/pip

Prepare virtual environment
###########################

With virtualenv/pip:

.. code-block:: sh

    git clone git@github.com:EYRA-Benchmark/eyra-tools.git
    cd eyra-tools
    virtualenv eyra_venv
    source eyra_venv/bin/activate
    pip install -r requirements.txt
    pip install -e .
