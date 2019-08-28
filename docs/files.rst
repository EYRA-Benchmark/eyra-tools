What are all the files?
-----------------------

Implementation
##############

* ``src/``: directory for storing code your algorithm needs.
* ``src/submission.py`` or ``src/evaluation.py``: Python file for developing the
  submission or evaluation code. Can be run locally on a copy of the benchmark data.
* ``src/run_submission.py`` or ``src/run_evaluation.py``: Python file containing the
  code for running a submission or evaluation inside the Docker container.
* ``requirements.txt``: file for listing the Python packages your algorithm depends on.

Local data handling
###################

* ``data/input/``: local directory used to read the input data from.
* ``data/input/test_data``, ``data/input/ground_truth``, and/or
  ``data/input/implementation_output``: example data for the boilerplate
  submission or evaluation. These files need to be replaced with data from the
  benchmark.
* ``data/``: local directory for storing the output of the algorithm.
* ``data/output_data_appears_here.txt``: example file to show where the
  local output is stored (feel free to delete this file).
* ``data/.gitignore`` and ``data/input/.gitignore``: configuration files to make
  sure the data directories are created on your computer. If you are using git
  for version control, these files also ensure that data files are not stored in
  your repository.

Scripts
#######

* ``build.sh``: script for building the container (without running
  the code).
* ``test.sh``: script for building the container and running the code.
* ``push.sh``: script for submitting the algorithm to the EYRA Benchmark Platform.
* ``export.sh``: script for exporting the image of your container to tar file.

.. note::
   ``export.sh`` is currently not used. Alternative ways of submitting
   Docker containers will be added to the EYRA Benchmark Platform later.

Miscellaneous
#############

* ``Dockerfile``: specifies the Docker container. If your algorithm
  only uses Python packages, there is no need to change this file.