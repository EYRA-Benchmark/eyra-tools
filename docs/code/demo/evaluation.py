import json
from pathlib import Path

import pandas as pd

from sklearn import metrics


def evaluate_iris(submission_file, test_gt_file, out_file):
    df = pd.read_csv(test_gt_file)
    test_gt = df['class'].to_list()

    df = pd.read_csv(submission_file)
    pred = df['class'].to_list()

    prec = metrics.precision_score(test_gt, pred, average='weighted')
    recall = metrics.recall_score(test_gt, pred, average='weighted')
    f = metrics.f1_score(test_gt, pred, average='weighted')

    out = {'metrics': {'Precision': prec,
                       'Recall': recall,
                       'F1': f}}
    with open(out_file, 'w') as f:
        json.dump(out, f)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python src/evaluation.py

    # These are the default file paths (names) for input and output, so don't
    # change them.
    submission_file = str(Path('data')/'input'/'implementation_output')
    test_gt_file = str(Path('data')/'input'/'ground_truth')
    out_file = str(Path('data')/'output')

    evaluate_iris(submission_file, test_gt_file, out_file)
