User Manual
-----------

If you want to participate in a benchmark on the EYRA Benchmark Platform, you
need to create a model based on participant data, that can predict outcomes
(e.g., class labels or numeric values) given test data. What you submit to the
benchmark platform is a Docker container that does the predictions, given your
model or algorithm.
Benchmark organisers need to provide a Docker container for evaluating the
results produced by the models/algorithms of participants.
The EYRA tools can be used to generate boilerplate containers that set up
as much as possible, so you can focus on implementing the prediction algorithm
or evaluation metrics.

To be able to use the Docker container as an submission or evaluation, you need
to publish it on `Docker Hub`_. If you (or your organization) do(es) not yet have a
Docker Hub account, you need to `sign up <https://hub.docker.com/signup>`_ for one.

Quickstart
##########

1. Generate a boilerplate container by running:
   ``eyra-generate [submission|evaluation] <name>``. A directory called
   ``<name>`` is created.
2. Put the input data in the ``<name>/data/input/`` directory.

   - Benchmark participants should download the public test data and put it
     in this directory. The file should be called ``data/input/test_data``.
   - Benchmark organisers should create an example output file in the same format
     as the ground truth and put them in the ``data/input/`` directory.
     The files should be called ``data/input/implementation_output`` and
     ``data/input/ground_truth`` respectively.

3. For submissions, implement the prediction code in ``src/submission.py``.
   For evaluations, implement evaluation metrics in ``src/evaluation.py``.
   You can test your code by running ``python src/submission.py`` or
   ``python src/evaluation.py`` from the ``<name>`` directory.
   Output is written to ``<name>/data/output``.

   .. important::
       Please do not change the file paths in the part of the code after
       ``if __name__ == "__main__":``. Running submissions and evaluations
       depends on default file names. When running the container locally
       (see step 7 of this quickstart), these paths are mapped to your local
       copy of the input and output directories. When running on the benchmark
       platform, they are mapped to the challenge input and output directories.

4. Add any file you need to the ``<name>/src`` directory. This can be (Python)
   code, but also (binary) files containing a model (see
   :ref:`the tutorial<iris:Demo benchmark: the Iris data>` for an example).
   For evaluations, you might not need additional files.
5. Add your code's dependencies to the ``<name>/requirements.txt`` file.
6. Update the ``run()`` method of the ``Submission`` or ``Evaluation`` object
   to call a function or functions from ``src/submission.py`` or
   ``src/evaluation.py``.

   .. tip::
       The generated code contains a complete, albeit very simple, example of a
       submission or evaluation. For a more realistic example have a look at the
       :ref:`demo benchmark tutorial<iris:Demo benchmark: the Iris data>`.

7. Test your container by running ``test.sh``. This will build the container
   and run the prediction or evaluation code on your local copy of the data.
   Output is written to ``<name>/data/output``.
8. If you are done developing, run the ``push.sh`` script to tag your Docker
   container with a version number and push it to `Docker Hub`_.

   .. code-block:: sh

       ./push.sh [version]

   If you omit the version number, the Docker image is tagged with ``latest``.
9. Specify the Docker container using ``<docker hub account>/<name>:<version>``
   on the EYRA Benchmark Platform.

Complete example
################

After :ref:`installing the EYRA Tools<installation:Installation>`, and acquiring
a `Docker Hub`_ account, generate a
boilerplate container by running:

.. code-block:: sh

    eyra-generate [submission|evaluation] <name> [-d <docker hub account>]

For submissions, this will create a directory with the following structure:

.. code-block:: sh

    <name>
    ├── .gitignore
    ├── Dockerfile
    ├── README.md
    ├── build.sh
    ├── data
    │   ├── .gitignore
    │   ├── input
    │   │   ├── .gitignore
    │   │   └── test_data
    │   └── output_data_appears_here.txt
    ├── export.sh
    ├── push.sh
    ├── requirements.txt
    ├── src
    │   ├── run_submission.py
    │   └── submission.py
    └── test.sh

For evaluations, the file names are slightly different:

.. code-block:: sh

    <name>
    ├── .gitignore
    ├── Dockerfile
    ├── README.md
    ├── build.sh
    ├── data
    │   ├── .gitignore
    │   ├── input
    │   │   ├── .gitignore
    │   │   ├── ground_truth
    │   │   └── implementation_output
    │   └── output_data_appears_here.txt
    ├── export.sh
    ├── push.sh
    ├── requirements.txt
    ├── src
    │   ├── evaluation.py
    │   └── run_evaluation.py
    └── test.sh

For more information on what the files and directories are used for, have a look
at :ref:`files:What are all the files?`

.. tip::
    It is good practice to use version control when writing code. Now is a good time
    to do so. If you are using git, run:

    .. code-block:: sh

        git init
        git add -A
        git commit -m "Initial commit"

.. Note::
    It is also good practice to separate code and data. However, because the
    boilerplate container contains a bash script for running the code inside the
    Docker container, it
    is convenient to have the data in the directory generated by running
    ``eyra-generate`` (otherwise you
    wouldn't be able to run ``test.sh`` on another computer). To prevent the
    data from being uploaded to github or another Git repository hosting
    service, the ``data`` directory is ignored by git.

################
Data preparation
################

The boilerplate code comes with example data. The data files can be found in the
``data/input`` directory. For submissions, there is a single data file called
``test_data`` and for evaluations there are two files, ``ground_truth`` and
``implementation_output``.
Both submissions and evaluations should produce a single file called ``output``,
that is written to the ``data`` directory.

.. important::
    As the EYRA Benchmark Platform uses these default file names, do not change
    them when working on your own submission or evaluation!

For a submission, you can get the data files from the benchmark page on the EYRA
Benchmark Platform. For evaluations, it is the responsability of the benchmark
organizers to prepare the data files.

##############
Implementation
##############

All files related to your algorithm should be put in the ``src`` directory.
Because for development and debugging it is easier to run the code on
your computer instead of inside the Docker container, the code is divided over
two files: ``submission.py`` and ``run_submission.py``
for submissions and ``evaluation.py`` and ``run_evaluation.py`` for evaluations.

``<container_type>.py`` contains the functionality for running the submission or
evaluation and ``run_<container_type>.py`` contains the code for running the
submission or evaluation inside the Docker container.
``submission.py`` looks like:

.. literalinclude:: code/submission.py
   :language: python
   :linenos:

The code contains a single function ``my_submission()`` that takes two arguments:
a path to the input file (i.e., ``data/input/test_data``) and a path to the
output file (i.e., ``data/output``) (line 7). On line 8 and 9, the test data
is read and put into a numpy array. Next, the output file is opened for writing
(line 11) and we loop over the values in the test data. The example prediction
algorithm is very simple: for every value in the test data, we write a zero to
the output file if the number is even and a one if the number is odd.

The code can be run by typing ``python src/submission.py``. If you do that,
everything after line 17 is excecuted. First, we create file paths for the input
and output file (lines 23 and 24). Then ``my_submission()`` is called.

After running the code, the ``data`` directory contains a new file called
``output``.

The boilerplate code for evaluations (``evaluation.py``) is very similar:

.. literalinclude:: code/evaluation.py
   :language: python
   :linenos:

The main function is called ``my_evaluation()`` and requires three arguments:
the submission file (i.e., ``data/input/implementation_output``), the ground
truth (i.e., ``data/input/ground_truth``), and the output file (i.e.,
``data/output``). On lines 11 and 12 and 13 and 14, the input files are read into
numpy arrays. For the evaluation, we are going to count how often the numbers in
both arrays are the same. We set a counter to zero (line 16), and loop over the
numbers in both arrays simultaneously (line 17). If the numbers are equal (line 18)
we add one to the counter (line 19). Next, we prepare the output. The output
should be a json file containing a single object (dictionary) with a ``metrics``
key. The value of ``metrics`` is an object (dictionary) listing the names of the
metrics and their value. In this case, we have a single value called ``accuracy``
for which we calculate the value by taking the number of samples for which the
predicted label was equal to the gold standard and dividing by the total number
of samples. On lines 23 and 24, this data is written to ``data/output``.

If you are done implementing your submission or evaluation code, it is time to
make sure it can be run inside the Docker container. In order to do so, you need
to update ``run_submission.py`` or ``run_evaluation.py``.

``run_submission.py`` looks like:

.. literalinclude:: code/run_submission.py
   :language: python
   :linenos:

On line 3, we import the ``my_submission()`` function from ``submission.py``,
which is called inside the ``Submission`` object's (line 5) ``run()`` method
(line 11) on line 11. For your submission, change the code to import the
function(s) needed to create the output, and call them in the ``run()`` method.

If you need to split up your code into multiple Python files or if you need
additional files for predicting outcomes, put them in the ``src``
directory, and load them inside the ``run()`` method (see
:ref:`iris:Demo benchmark: the Iris data` for an example).

.. warning::
    If you change the code below line 14, you run the risk that it will not work
    on the EYRA Benchmark Platform.

.. note::
    This is the code for submissions. The code for evaluations looks slightly
    different. For evaluations line 5 is ``class Evaluation(object):`` and
    the ``run()`` method has three arguments (i.e., the submission file, the
    ground truth file, and the output file) instead of two.

.. important::
    When running the Docker container locally, the input and output directory on your
    hard drive are mapped to ``/data/input/`` and ``/data/`` using docker.
    When running it on the benchmark platform, these directories are mapped
    to the benchmark input and output directories.

##############
Output formats
##############

For submissions, the benchmark page should specify the output format.
For evaluations, the output should be a json file containing:

.. code-block:: sh

    {
        "metrics": {
            "metric1": <numeric value>
            ...
        }
    }

############
Dependencies
############

All dependencies (like ``numpy`` (line 5) in the example submission), should be
listed in ``requirements.txt``, so they are installed inside the container.

#############################
Building the Docker container
#############################

To build the Docker container, run ``build.sh``.

.. code-block:: sh

    $ ./build.sh
    Sending build context to Docker daemon  31.74kB
    Step 1/7 : FROM python:3.7-slim
    ---> 783362c5ef81
    Step 2/7 : RUN mkdir -p /opt/src /input /output
    ---> Using cache
    ---> 5cf2874fe9d2
    Step 3/7 : WORKDIR /opt/src
    ---> Using cache
    ---> 4876a0b73b86
    Step 4/7 : COPY requirements.txt /opt/src/
    ---> Using cache
    ---> d397b4c2f203
    Step 5/7 : RUN python -m pip install -r requirements.txt
    ---> Using cache
    ---> b7815db6c39e
    Step 6/7 : ADD src /opt/src/
    ---> Using cache
    ---> e6ea2d81fb51
    Step 7/7 : ENTRYPOINT "python" "-m" "run_submission"
    ---> Using cache
    ---> 013e85d0112d
    Successfully built 013e85d0112d
    Successfully tagged <name>:latest

If you want to build the Docker container and test your code, run ``test.sh``.

Have a look at the :ref:`scripts page<scripts:Scripts>` for an overview
of the scripts available for manipulating the Docker container.

###################
Tagging and pushing
###################

If you are done developing, run the ``push.sh`` script to tag your Docker
container with a version number and push it to `Docker Hub`_.

.. code-block:: sh

    ./push.sh [version]

If you omit the version number, the Docker image is tagged with ``latest``.

.. warning::
    Please use `semantic versioning <https://semver.org>`_ rather
    than the ``latest`` tag. If you submit ``latest`` Docker images, the
    EYRA Benchmark Platform might not use the latest version.

.. tip::
    If you get the following message: ``denied: requested access to the
    resource is denied`` ``unauthorized: authentication required``.
    You need to login to Docker Hub using ``docker login``.

You can also manually tag and push your image:

.. code-block:: sh

    docker tag <name/id> <docker hub account>/<name>:<version>
    docker push <docker hub account>/<name>

##########
Submitting
##########

To submit a submission or evaluation to the EYRA Benchmark Platform, put
``<docker hub account>/<name>:<version>`` in the designated form field.


.. _Docker Hub: https://hub.docker.com
