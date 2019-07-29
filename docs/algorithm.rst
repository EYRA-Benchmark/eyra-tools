Implementing an Algorithm
-------------------------

If you want to participate in a challenge on the EYRA Benchmark Platform, you
need to submit a Docker container that is able to run an algorithm and
benchmark organisers need to provide a Docker container for evaluating the
results produced by the algorithms of participants.
The EYRA tools can be used to generate a boilerplate container to setup up
everything, so you can focus on implementing your algorithm or evaluation
metrics.

Quickstart
##########

1. Generate a boilerplate container by running:
   ``eyra-generate [submission|evaluation] <name>``. A directory called
   ``<name>_<identifier>`` is created.
2. Put the input data in the ``<name>_<identifier>/data/input/`` directory.

   - Benchmark participants should download the training data and put it in
     this directory.
   - Benchmark organisers should create an example output file for their
     benchmark and put it in the ``data/input/`` directory.

3. Implement your algorithm in ``algorithm_src/algorithm.py``

.. important::
    Input data should be read from ``/input/``.
    Output should be written to ``/output/``. When running your container
    locally, these directories are mapped to your local copy of the input and
    output directories. When running on the benchmark platform, they are mapped
    to the challenge input and output directories.

4. Add your algorithm's dependencies to the
   ``<name>_<identifier>/requirements.txt`` file.
5. Test your algorithm by running ``test.sh``. This will build the container
   and run the algorithm on the local copy of the data. Output is written to the
   ``<name>_<identifier>/data/output`` directory.
6. If you are done developing, submit your algorithm by running ``push.sh``.

.. todo::
    Specify how benchmark organizers can submit their evaluation algorithms.

Complete example
################

After :ref:`installing the EYRA Tools<installation:Installation>`, generate a
boilerplate container by running:

.. code-block:: sh

    eyra-generate [submission|evaluation] <name>


This will create a directory with the following structure:

.. code-block:: sh

    <name>_<identifier>
    ├── Dockerfile
    ├── algorithm_src
    │   └── algorithm.py
    ├── build.sh
    ├── data
    │   ├── input
    │   │   └── example_input_data.txt
    │   └── output
    │       └── output_data_appears_here.txt
    ├── push.sh
    ├── requirements.txt
    └── test.sh

For more information on what the files and directories are used for, have a look
at `files:What are all the files?`.

It is good practice to use version control when writing code. Now is a good time
to do so. If you are using git, run:

.. code-block:: sh

    git init
    git add -A
    git commit -m "Initial commit"


##########################################################
Implement your algorithm in ``algorithm_src/algorithm.py``
##########################################################

All code related to your algorithm should be put in the ``algorithm_src`` directory.
It currently contains a single Python file called ``algorithm.py``:

.. literalinclude:: algorithm.py
   :language: python
   :linenos:

.. note::
    This is the code for submissions. The code for evaluations looks slightly
    different. For evaluations line 5 is ``class Evaluation(object):`` and
    line 24 is ``Evaluation().run()``.

Implement your algorithm in the ``run`` method of the ``Submission`` or
``Evaluation`` class.
Input should be read from ``/input/`` and output should be written to ``/output/``.

.. important::
    When running the algorithm locally, the input and output directory on your
    hard drive are mapped to ``/input/`` and ``/output/`` using docker.
    When running it on the benchmark platform, these directories are mapped
    to the challenge input and output directories.

The boilerplate algorithm opens two files, one in the input directory (line 12)
and one in the output directory (line 13). It reads the lines from the input
file one by one (line 14) and tries to extract two floats from this line (lines
15 and 16). If a line does not contain two floats separated by whitespace, the
algorithm moves on to the next line (lines 17 and 18). If floats were extracted,
they are used to calculate new values that are written to the output file (line 19).

Replace the code from lines 10-19 with your algorithm.

If you need to split up your code in multiple Python files, put them in the
``algorithm_src`` directory. This directory is copied into the container.

########################################
Put dependencies in ``requirements.txt``
########################################

Al dependencies (like ``numpy`` (line 2)) in the example algorithm, should be
listed in ``requirements.txt``, so they are installed inside the container.

######################################
To test your algorithm run ``test.sh``
######################################

If you want to test your algorithm, run ``test.sh``. This bash script builds
the container and then runs the algorithm.

Have a look at the :ref:`scripts page<scripts:Scripts>` for an overview
of the scripts available for manipulating the Docker container.

Additional instructions for creating evaluations
################################################

.. todo::
    Specify the output format required by the leaderboard.

.. todo::
    Specify what to do in case of multiple metrics (how to rank these).
