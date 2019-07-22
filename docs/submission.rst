Submission
----------

Meant for algorithm developers.

Create submission project
#########################

.. code-block:: sh

    eyra_submission init <submission_name>

This will create a folder with all boilerplate code to start building an algorithm container.

Develop
#######

- add all your algorithm's dependencies to the ``<submission_name>/requirements.txt`` file
- add your algorithm's code to the run method in the ``algorithm_src/algorithm.py`` module (remember the imports)
- add your input data to the ``test-input-data`` folder
- Due to the infrastructure (docker), these folders will be renamed from the algorithm's perspective.

.. warning::
    Please write your code so the input data is read from the ``/input/`` folder and the output data is written to
    the ``/output/`` folder.

- any other files that your algorithm depends on should be placed in the ``algorithm_src`` folder

- to run the algorithm, execute the ``test.sh`` script: this will create a Docker container with your algorithm in it, and run it
- the output data can be found in the ``test-output-data`` folder

Build, export and push
######################

To build the docker image of your algorithm, use the ``build.sh`` script. To export the image to a tar file, use
the ``export.sh`` script. To upload the algorithm image to the EYRA docker registry, use the ``push.sh`` script.
