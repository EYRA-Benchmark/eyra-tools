import pandas as pd

from pathlib import Path

from sklearn import svm


def train_svm(in_file):
    # Read the training file
    train = pd.read_csv(in_file)

    train_data = train[['sepal_length', 'sepal_width', 'petal_length',
                        'petal_width']].values
    train_targets = list(train['class'])

    # Train the classifier
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(train_data, train_targets)

    return clf


def predict(clf, test_data_file):
    test = pd.read_csv(test_data_file)

    return clf.predict(test.values)


def iris_svm(train_file, test_file, out_file):
    """Train Support Vector Machines for the EYRA Demo Benchmark.
    """
    # Train classifier
    clf = train_svm(train_file)

    # Predict
    pred = predict(clf, test_file)

    print(pred)

    output = pd.DataFrame()
    output['class'] = pred

    # Write the output to file
    output.to_csv(out_file)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_scr/algorithm.py
    train_file = Path('data')/'input'/'iris_train.csv'
    test_file = Path('data')/'input'/'iris_public_test_data.csv'
    out_file = Path('data')/'output'/'team_eyra.csv'

    iris_svm(train_file, test_file, out_file)
