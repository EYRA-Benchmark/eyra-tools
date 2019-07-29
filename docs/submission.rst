Submission
----------

If you want to participate in a challenge on the EYRA Benchmark Platform, you
need to submit a Docker container that is able to run your algorithm.
The EYRA tools can be used to generate a boilerplate container to setup up
everything, so you can focus on implementing your algorithm.

Quickstart
##########

1. Generate a boilerplate algorithm container by running:
   ``eyra_submission init <submission_name>``. A directory called
   ``<submission_name>_<identifier>`` is created.
2. Download the training data for your challenge, unzip the files if necessary,
   and put them in the ``<submission_name>_<identifier>/data/input/`` directory.
3. Implement your algorithm using ``algorithm_src/algorithm.py``

.. important::
    Input data should be read from ``/input/``.
    Output should be written to ``/output/``. When running your container
    locally, these directories are mapped to your local copy of the input and
    output directories. When running on the benchmark platform, they are mapped
    to the challenge input and output directories.

4. Add your algorithm's dependencies to the
   ``<submission_name>_<identifier>/requirements.txt`` file.
5. Test your algorithm by running ``test.sh``. This will build the container
   and run the algorithm on the local copy of the data. Output is written to the
   ``<submission_name>_<identifier>/data/output`` directory.
6. If you are done developing, submit your algorithm by running ``push.sh``.

Complete example
################

After :ref:`installing the EYRA Tools<Installation>`, generate a boilerplate container by running:

.. code-block:: sh

    eyra_submission init <submission_name>


This will create a directory with the following structure:

.. code-block:: sh

    <submission_name>_<identifier>
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

Implement your algorithm in the ``run`` method of the ``Submission`` class.
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

For the example container, the following output is produced:

.. code-block:: sh

    > ./test.sh
    Sending build context to Docker daemon  26.62kB
    Step 1/7 : FROM python:3.7-slim
    ---> 63491ee411bb
    Step 2/7 : RUN mkdir -p /opt/algorithm /input /output
    ---> Using cache
    ---> c3ff6ef64ade
    Step 3/7 : WORKDIR /opt/algorithm
    ---> Using cache
    ---> bb353791430a
    Step 4/7 : COPY requirements.txt /opt/algorithm/
    ---> Using cache
    ---> e1d53a90caf5
    Step 5/7 : RUN python -m pip install -r requirements.txt
    ---> Using cache
    ---> e38a671df8e1
    Step 6/7 : ADD algorithm_src /opt/algorithm/
    ---> e9e676d15a16
    Step 7/7 : ENTRYPOINT "python" "-m" "algorithm"
    ---> Running in 351b9fae7bd9
    Removing intermediate container 351b9fae7bd9
    ---> 03e14ac75917
    Successfully built 03e14ac75917
    Successfully tagged <submission_name>_<identifier>:latest


########################################
To build your algorithm run ``build.sh``
########################################

If you want to test whether your Docker container can be built, but you don't
want to run the algorithm, use the the ``build.sh`` script.

########################################
To submit your algorithm run ``push.sh``
########################################

If you are done with implementing your algorithm, and want to submit it to the
challenge, run ``push.sh``. The container will be built and submitted to the
EYRA Benmark Platform.

#####################################
To export the image run ``export.sh``
#####################################

You can export the Docker image to a tar file by running the ``export.sh`` script.

What are all the files?
#######################

##############
Implementation
##############

* ``algorithm_src/``: directory for storing code your algorithm needs.
* ``algorithm_src/algorithm.py``: main file containing the implementation of the algorithm.
* ``requirements.txt``: file for listing the Python packages your algorithm depends on.

###################
Local data handling
###################

* ``data/input/``: local directory used to read the input data from.
* ``data/input/example_input_data.txt``: example data for the boilerplate
  algorithm (feel free to delete this file).
* ``data/output/``: local directory for storing the output of the algorithm.
* ``data/output/output_data_appears_here.txt``: example file to show where the
  local output is stored (feel free to delete this file).

#######
Scripts
#######

* ``build.sh``: script for building the algorithm container (without running
  the algorithm).
* ``test.sh``: script for building the container and running the algorithm.
* ``push.sh``: script for submitting the algorithm to the EYRA Benchmark Platform.
* ``export.sh``: script for exporting the image of your container to tar file.

#############
Miscellaneous
#############

* ``Dockerfile``: specifies the algorithm container. If your algorithm
  only uses Python packages, there is no need to change this file.