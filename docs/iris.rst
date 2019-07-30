Demo benchmark: the iris data
-----------------------------

This is a demo benchmark set up to show potential benchmark organisers what
needs to be done to set up a benchmark on the EYRA Benchmark Platform and to
allow potential benchmark participants to try submitting an algorithm.

The demo benchmark uses the iris dataset. The iris dataset is a multivariate
dataset containing measurements of the petals and sepals of different types of
irises. The task is to predict the species of Iris (Setosa, Virginica, or
Versicolor) based on the length and width of petals and sepals.

* Train and test set (division and explanation)

For participants: creating a submission
#######################################

1. Download the data from the demo benchmark.

.. todo::
  Add link to the demo benchmark.

2. Implement your algorithm. For the demo, we are keeping things simple and
   implement Support Vector Machines using scikit-learn. The code looks like:

   .. literalinclude:: code/algorithm.py
      :language: python
      :linenos:

   In line 1-5 we import the Python libraries we need. Line 8 defines the function
   for running our algorithm. It is a good idea to have a separate function that
   runs the algorithm from beginning to end, and that has as input parameters the
   training data file and the output file or, in this case, directory. This way,
   it is easy to run the our algorithm during development (lines 34-37), and it is
   also easy to start the algorithm from another Python file, which is what we need
   later.

   We read the training data and add the column names in lines 12 and 13.
   After that, we convert the class labels, which are strings (Iris-setosa,
   Iris-versicolor, and Iris-virginica) to integers using scikit-learn's
   LabelEncoder.
   Next, we train the classifier (lines 21-22) and predict labels for the test data
   (lines 26-29). In line 29, we convert the predicted integer classes back to the
   original strings.
   Finally, the output data is written to a file (line 32).

   .. note::
      When implementing your own algorithm, feel free to use more functions and
      Python files if needed. For complicated code it might be a good idea to
      create your own Python package.

3. During implementation, you can test your algorithm by running ``python algorithm.py``.
   Make sure to update the file paths in line 35 and 36, so they point to the
   copy of the iris data on your computer and a directory for writing the output.
4. If you are satisfied with your algorithm, generate a boilerplate submission
   container using the [EYRA Tools](), cd into the directory that is generated,
   and copy the data and your algorithm code into the boilerplate container:

   .. code-block:: sh

       eyra-generate submission iris
       cd iris_<identifier>
       cp ~/Downloads/iris.data data/input/.
       cp ~/code/iris_svm/algorithm.py algorithm_src/.

   The file paths from which files are copied need to be changed to the correct
   paths on your computer.
5. Add all Python libraries needed to run your algorithm to ``requirements.txt``.
   For the demo we add ``pandas`` and ``scikit-learn``.
6. Set the file paths in lines 35 and 36 of ``algorithm_src/algorithm.py`` to
   ``data/input/iris.data`` and ``data/output/``. You can now run the algorithm
   on your computer by typing: ``python algorithm_src/algorithm.py``.
7. To build the Docker container and run the algorithm inside it, type ``./test.sh``.

.. todo::
    Show how the container can be submitted to the demo challenge.

For organisers: creating an evaluation
######################################
