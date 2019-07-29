What are all the files?
-----------------------

Implementation
##############

* ``algorithm_src/``: directory for storing code your algorithm needs.
* ``algorithm_src/algorithm.py``: main file containing the implementation of the algorithm.
* ``requirements.txt``: file for listing the Python packages your algorithm depends on.

Local data handling
###################

* ``data/input/``: local directory used to read the input data from.
* ``data/input/example_input_data.txt``: example data for the boilerplate
  algorithm (feel free to delete this file).
* ``data/output/``: local directory for storing the output of the algorithm.
* ``data/output/output_data_appears_here.txt``: example file to show where the
  local output is stored (feel free to delete this file).

Scripts
#######

* ``build.sh``: script for building the algorithm container (without running
  the algorithm).
* ``test.sh``: script for building the container and running the algorithm.
* ``push.sh``: script for submitting the algorithm to the EYRA Benchmark Platform.
* ``export.sh``: script for exporting the image of your container to tar file.

Miscellaneous
#############

* ``Dockerfile``: specifies the algorithm container. If your algorithm
  only uses Python packages, there is no need to change this file.