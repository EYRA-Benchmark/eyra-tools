Demo benchmark: the iris data
-----------------------------

This is a demo benchmark set up to show potential benchmark organisers what
needs to be done to set up a benchmark on the EYRA Benchmark Platform and to
allow potential benchmark participants to try submitting an algorithm.
All data and code used for this demo can be found `on github
<https://github.com/EYRA-Benchmark/eyra-iris-demo>`_.

.. figure:: diagrams/overview2.png
   :alt: Overview of the EYRA Benchmark Platform.

   Overview of the EYRA Benchmark Platform.

The figure above shows an overview of how things work with the EYRA Benchmark Platform.
It shows the data sets involved (participant data, which can or cannot be ground truth
data, and public test data and optionally private test data), the parts of the
benchmark done by the platform and the part of the benchmark that should be done
by benchmark participants.

Benchmark organizers make available different data sets, i.e., participant data
and public test data. This data is used by benchmark participants to create a
model. For the demo, this model is a machine learning model, but it is possible
to create other types of models (WOULD BE NICE TO INSERT A REFERENCE HERE WITH EXAMPLES).
As shown in the figure, creating the model is the responsibility of the participant,
and is not part of the EYRA Benchmark Platform. The demo model creation
code is in the ``model_creation`` directory. Usually, benchmarks have available
public test data that can be used to test the performance of the algorithm.

To participate in a benchmark, a participant should submit a Docker container
that can predict labels or other outcomes for test data, given the model
created in the previous step. To help them to get started, participants can
use the `EYRA Tools <https://github.com/EYRA-Benchmark/eyra-tools>`_
to create a boilerplate docker container.

The demo benchmark uses the iris dataset. The iris dataset is a multivariate
dataset containing measurements of the petals and sepals of different types of
irises. The task is to predict the species of Iris (Setosa, Virginica, or
Versicolor) based on the length and width of petals and sepals. The data set
was randomly dived into three sets containing 50 samples each; one set is used
as participant data, one set as public test data and one set as private test
data. See under `For organisers: creating a benchmark`_ for more details about
the creation of the datasets.

For participants: creating a submission
#######################################

1. Download the participant data and public test data from the `demo benchmark
<https://www.eyrabenchmark.net/benchmark/eebc5f91-be13-4433-9080-f920187b1982>`_.

   - Go to the `benchmark page <https://www.eyrabenchmark.net/benchmark/eebc5f91-be13-4433-9080-f920187b1982>`_.
   - Click Data.
   - Read the data description.
   - Download the files.

2. Create a model. For the demo, we are keeping things simple and
   train Support Vector Machines using scikit-learn. The code can be found in
   ``model_creation/train.py`` and looks like:

   .. literalinclude:: code/train.py
      :language: python
      :linenos:

   In line 1-8 we import the Python libraries we need. The model creation code consist
   of two functions. Generally speaking, it is a good idea to divide your code
   into multiple functions, e.g., one for data preprocessing, one for training,
   and one for making predictions.
   The function for training the model starts on line 11. It has as input
   parameter the participant data file. The function reads the participant data
   (line 16) and puts it into the format that is required by machine learning
   algorithms in scikit-learn (lines 18-20).
   Next, a Support Vector classifier is trained (lines 23-24) and returned (line 26).

   The ``save_model()`` function on line 29 takes as input a classifier and path
   and then saves the model to that path, so it can be saved in the submission
   docker container and used for predicting iris labels.

   The ``predict()`` function on line 33 can be used to test whether predicting
   labels given a test file works as expected. It has two input parameters, a
   trained classifier and the path to a test data file. The function reads the
   test data (line 34) and returns the predictions (line 36).

   .. note::
      When creating a model, feel free to use more functions and
      Python files if needed. For complicated code and if you want to be able to
      re-use for example data preprocessing functions, it might be a good idea to
      create your own Python package.

    .. todo::
        Add link to good tutorial about creating installable packages.

   During implementation, you can test your model by running ``python train.py``
   in the ``model_creation`` directory. Line 38 makes sure the code below runs
   only if you type that command. After doing some administrative work to determine
   where the input data can be found and output should be written (lines 41 and 42),
   we create the directory for writing the model to if it doesn't exist
   (lines 44-47).
   Next, we create variables that store the path to the input file (i.e. the
   participant data; line 49) and the path to the output file (line 50).
   On line 52 the classifier is trained, after which it is saved to a file
   (line 53).

   To test whether the model can be used for prediction, a variable containing the
   path to a test data file is created (line 56). Next, the ``predict()`` function
   is called and the result of that is printed to the screen.
   The ouput produced by running the train script looks like:

    .. code-block:: sh

      $ python model_creation/train.py
      ['Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
       'Iris-setosa' 'Iris-virginica' 'Iris-virginica' 'Iris-setosa'
       'Iris-setosa' 'Iris-versicolor' 'Iris-versicolor' 'Iris-setosa'
       'Iris-versicolor' 'Iris-versicolor' 'Iris-virginica' 'Iris-versicolor'
       'Iris-versicolor' 'Iris-versicolor' 'Iris-setosa' 'Iris-virginica'
       'Iris-virginica' 'Iris-setosa' 'Iris-versicolor' 'Iris-versicolor'
       'Iris-setosa' 'Iris-versicolor' 'Iris-setosa' 'Iris-versicolor'
       'Iris-virginica' 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica'
       'Iris-virginica' 'Iris-setosa' 'Iris-virginica' 'Iris-virginica'
       'Iris-setosa' 'Iris-virginica' 'Iris-setosa' 'Iris-virginica'
       'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-versicolor'
       'Iris-versicolor' 'Iris-virginica' 'Iris-versicolor' 'Iris-setosa'
       'Iris-setosa']

   This result tells us that the prediction mechanics work, but it doesn't say
   anything about performance. If you would like to estimate performance of your
   model using the participant data only, have a look at
   `cross-validation <https://machinelearningmastery.com/k-fold-cross-validation/>`_.
3. To be able to calculate actual performance of your model, you need to create
   a submission Docker container that contains a prediction algorithm.
   A boilerplate submission container can be generated using the `EYRA Tools
   <https://github.com/EYRA-Benchmark/eyra-tools>`_. Run ``eyra-generate
   submission demo_submission`` (after :ref:`installing the EYRA Tools<installation:Installation>`),
   cd into the directory that is generated,
   and copy the data into the boilerplate container:

   .. code-block:: sh

       eyra-generate submission demo_submission
       cd demo_submission_<identifier>
       cp ~/Downloads/iris_public_test_data.csv data/input/test_data
       mkdir algorithm_src/model
       cp ~/code/iris_svm/model/iris_svm_model algorithm_src/model/iris_svm_model

   It is probably a good idea to choose a better name than ``demo_submission``.
   Also, the file paths from which files are copied need to be changed to the correct
   paths on your computer.

   .. todo::
        Resolve file naming issues (the submission container expects input
        files with specific names and should produce output files with specific
        names. These names are different from what the files are called now).

4. Implement the prediction algorithm in ``algorithm_src/algorithm.py``.
   For the iris SVM this file looks like:

   .. literalinclude:: code/algorithm.py
      :language: python
      :linenos:

   The prediction algorithm has two functions, ``iris_svm_predict()`` (line 9)
   and ``predict()`` (line 22), which is the same as the ``predict()`` function
   we used during model creation. The ``iris_svm_predict()`` function first loads
   the model created during the previous step (line 11). It then predicts class
   labels given the model and the test data file (line 14). On line 17-19 a
   pandas DataFrame containing a single column called 'class' is created and
   written to a csv file.
   Starting from line 28, we see how these functions are called to generate the
   implementation output used to calculate performance. Line 32 defines a
   variable containing the path to the model file. Lines 36 and 37 define variables
   that contain the paths to the test data and output respectively. Finally, on
   line 39, the ``iris_svm_predict()`` function is called using the paths as
   arguments.
5. You can test the prediction algorithm by running ``python algorithm_src/algorithm.py``
   from the ``demo_submission_<identifier>`` directory. If everything works as
   expected, we can start with preparing the Docker container.
6. Add all Python libraries needed to run the prediction algorithm to ``requirements.txt``.
   For the demo we add ``pandas`` and ``scikit-learn``.
7. Update ``python algorithm_src/run_submission.py``, so it calls the
   ``iris_svm_predict()`` function:

  .. literalinclude:: code/run_submission.py
      :language: python
      :linenos:

   Compared to the boilerplate file, only a few lines were changed
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


