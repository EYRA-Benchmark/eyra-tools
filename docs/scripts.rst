Scripts
-------

``test.sh``
###########

If you want to test your container, run ``test.sh``. This bash script builds
the container and then runs the code.

For the example container, the following output is produced:

.. code-block:: sh

    $ ./test.sh
    Sending build context to Docker daemon  78.85kB
    Step 1/7 : FROM python:3.7-slim
    ---> f96c28b7013f
    Step 2/7 : RUN mkdir -p /opt/src /input /output
    ---> Using cache
    ---> 6bfe8fb274ca
    Step 3/7 : WORKDIR /opt/src
    ---> Using cache
    ---> 8e0b820ab7b7
    Step 4/7 : COPY requirements.txt /opt/src/
    ---> 02a8f551c536
    Step 5/7 : RUN python -m pip install -r requirements.txt
    ---> Running in 105f5db285be
    Collecting numpy==1.16.0 (from -r requirements.txt (line 1))
    Downloading https://files.pythonhosted.org/packages/3d/10/62224c551acfd3a3583ad16d1e0f1c9e9c333e74479dc51977c31836119c/numpy-1.16.0-cp37-cp37m-manylinux1_x86_64.whl (17.3MB)
    Installing collected packages: numpy
    Successfully installed numpy-1.16.0
    Removing intermediate container 105f5db285be
    ---> 1a0307108b9a
    Step 6/7 : ADD src /opt/src/
    ---> 2339ef697553
    Step 7/7 : ENTRYPOINT "python" "-m" "run_submission"
    ---> Running in a01619750047
    Removing intermediate container a01619750047
    ---> 49effc50d7a4
    Successfully built 49effc50d7a4
    Successfully tagged <name>:latest


``build.sh``
############

If you want to test whether your Docker container can be build, but you don't
want to run the code, use the the ``build.sh`` script.

``push.sh``
###########

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

.. todo::
    Specify how benchmark organizers can submit their evaluation algorithms.

``export.sh``
#############

You can export the Docker image to a tar file by running the ``export.sh`` script.

.. note::
   ``export.sh`` is currently not used. Alternative ways of submitting
   Docker containers will be added to the EYRA Benchmark Platform later.

.. _Docker Hub: https://hub.docker.com
