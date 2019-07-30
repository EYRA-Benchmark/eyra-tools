import pandas as pd

from pathlib import Path

from sklearn import preprocessing, svm


def iris_svm(in_file, out_dir):
    """Train Support Vector Machines for the EYRA demo benchmark.
    """
    # Read the training file
    train = pd.read_csv(in_file, header=None)
    train.columns = ['sepal_length', 'sepal_width', 'petal_length',
                     'petal_width', 'class']

    # Convert string class labels to integers
    le = preprocessing.LabelEncoder()
    targets = le.fit_transform(train['class'])

    # Train the classifier
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(train[['sepal_length', 'sepal_width', 'petal_length',
                   'petal_width']].values, targets)

    # Predict using the test data
    pred = clf.predict(train[['sepal_length', 'sepal_width', 'petal_length',
                              'petal_width']].values)
    output = pd.DataFrame()
    output['class'] = le.inverse_transform(pred)

    # Write the output to file
    output.to_csv(Path(out_dir) / 'team_eyra.csv')

if __name__ == "__main__":
    in_file = Path('data') / 'input' / 'iris.data'
    out_dir = Path('data') / 'output'
    iris_svm(in_file, out_dir)
