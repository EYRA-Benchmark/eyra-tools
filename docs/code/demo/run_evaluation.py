from pathlib import Path

from evaluation import evaluate_iris


class Evaluation(object):
    def run(self, submission_file, test_gt_file, out_file):
        """This is boilerplate. Delete the contents of this method and put your
        own code here. Please do not change the class name (Evaluation),
        the method name (run), or the arguments.
        """
        evaluate_iris(submission_file, test_gt_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    # These are the default file paths (names) for input and output
    submission_file = Path('/')/'data'/'input'/'implementation_output'
    test_gt_file = Path('/')/'data'/'input'/'ground_truth'
    out_file = Path('/')/'data'/'output'

    Evaluation().run(submission_file, test_gt_file, out_file)
