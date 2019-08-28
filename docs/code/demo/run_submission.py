import os
from pathlib import Path

from submission import iris_svm_predict


class Submission(object):
    def run(self, test_file, out_file):
        # Additional data required by the prediction algorithm
        model_file = Path(__file__).absolute().parent/'model'/'iris_svm_model'

        iris_svm_predict(model_file, test_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    # These are the default file paths (names) for input and output
    test_file = Path('/')/'data'/'input'/'test_data'
    out_file = Path('/')/'data'/'output'

    Submission().run(test_file, out_file)
