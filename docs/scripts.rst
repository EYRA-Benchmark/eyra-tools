Scripts
-------

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
    Successfully tagged <name>_<identifier>:latest


To build your algorithm run ``build.sh``
########################################

If you want to test whether your Docker container can be built, but you don't
want to run the algorithm, use the the ``build.sh`` script.

To submit your algorithm run ``push.sh``
########################################

If you are done with implementing your algorithm, and want to submit it to the
challenge, run ``push.sh``. The container will be built and submitted to the
EYRA Benmark Platform.

.. todo::
    Specify how benchmark organizers can submit their evaluation algorithms.

To export the image run ``export.sh``
#####################################

You can export the Docker image to a tar file by running the ``export.sh`` script.

