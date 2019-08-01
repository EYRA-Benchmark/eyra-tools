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
* https://github.com/EYRA-Benchmark/eyra-iris-demo

For participants: creating a submission
#######################################

1. Download the participant data and public test data from the demo benchmark.

   - Go to the benchmark page.
   - Click Data.
   - Read the data description.
   - Download the files.

.. todo::
  Add link to the demo benchmark.

2. Implement your algorithm. For the demo, we are keeping things simple and
   implement Support Vector Machines using scikit-learn. The code looks like:

   .. literalinclude:: code/algorithm.py
      :language: python
      :linenos:

   In line 1-5 we import the Python libraries we need. The algorithm code consist
   of three functions. Generally speaking, it is a good idea to divide your algorithm
   into multiple functions, e.g., one for data preprocessing, one for training,
   one for making predictions, and one for running the complete algorithm from
   beginning to end.
   The function for running the complete algorithm (for the example code, this
   function starts on line 29) should have as input parameters the
   training data file and the output file. This way,
   it is easy to run the our algorithm during development (lines 47-54), and it is
   also easy to start the algorithm from another Python file, which is what we need
   later.

   For our example algorithm, we don't need preprocessing, so there are two other
   functions, one for training the Support Vector Machines (starting on line 8) and
   one for making predictions (starting on line 23).

   The ``iris_svm()`` function first calls ``train_svm()`` (line 32). This function reads
   the participant data file on line 10. After that, variables containing the
   training data and the target class labels are created (line 12-13 and 14).
   Next, the classifier is trained (lines 17-18) and returned (line 20).
   The ``iris_svm()`` function continues with calling ``predict()`` (line 36).
   In ``predict()`` the test data is read (line 24). The function returns the
   classifier's predictions for the test data (line 26).
   The predictions are printed to the screen (line 38) and an pandas DataFrame
   containing the predictions is created (lines 40-41).
   Finally, the DataFrame is written to a CSV file (line 44).

   .. note::
      When implementing your own algorithm, feel free to use more functions and
      Python files if needed. For complicated algorithms it might be a good idea to
      create your own Python package.

3. During implementation, you can test your algorithm by running ``python algorithm.py``.
   Make sure to update the file paths in line 50-52, so they point to the
   copy of the iris data on your computer and a place where the output file can be written.
4. If you are satisfied with your algorithm, generate a boilerplate submission
   container using the `EYRA Tools <https://github.com/EYRA-Benchmark/eyra-tools>`_,
   cd into the directory that is generated,
   and copy the data and your algorithm code into the boilerplate container:

   .. code-block:: sh

       eyra-generate submission demo_submission
       cd demo_submission_<identifier>
       cp ~/Downloads/iris_train.csv data/input/.
       cp ~/Downloads/iris_public_test_data.csv data/input/.
       cp ~/code/iris_svm/algorithm.py algorithm_src/.

   It is probably a good idea to choose a better name than ``demo_submission``
   for your submission.
   Also, the file paths from which files are copied need to be changed to the correct
   paths on your computer.
5. Add all Python libraries needed to run your algorithm to ``requirements.txt``.
   For the demo we add ``pandas`` and ``scikit-learn``.
6. Set the file paths in lines 50-52 of ``algorithm_src/algorithm.py`` to
   ``data/input/iris_train.csv``, ``data/input/iris_public_test_data.csv``
   and ``data/output/team_iris.csv``. You can now run the algorithm
   on your computer by typing: ``python algorithm_src/algorithm.py``.
7. To build the Docker container and run the algorithm inside it, type ``./test.sh``.
8. If everything works as expected, you can submit your container to the benchmark.

.. todo::
    Show how the container can be submitted to the benchmark.

For organisers: creating a benchmark
####################################

To set up a benchmark on the EYRA Benchmark Platform you should
`contact the EYRA Benchmark team <mailto:info@eyrabenchmark.net>`_, and we will
get back to you with more specific instructions. In addition to thorough and
consise descriptions of the task, the data, the ground truth, and the evaluation
metrics (`see the benchmarks on the platform for examples
<https://www.eyrabenchmark.net/benchmarks>`_), organizers need to provide:

* Participant data
* Public test data + public test ground truth: this is the data used for creating
  the public leaderboard.
* Private test data + private test ground truth: this is hold-out data, that is
  used for creating the private leaderboard.
* A Docker container containing the evaluation algorithm. Have a look at
  :ref:`the tutorial<iris:For organisers: creating an evaluation>` to see how this is done.

.. note::
  For demonstration purposes, the demo benchmark's data is available on
  `github <https://github.com/EYRA-Benchmark/eyra-iris-demo>`_).
  For a real benchmark, the public test ground truth, and the private test data
  and ground truth should not be shared with participants. This helps to
  `make sure participants' submissions focus on understanding the problem and
  advancing science rather than incrementally improving metrics <https://arxiv.org/abs/1811.03014>`_.

For organisers: creating an evaluation
######################################

1. Create an evaluation script that reads all files in a directory and calculates
   F1-score for each file based on gold standard data:


