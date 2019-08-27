{%- if cookiecutter.container_type == 'evaluation' -%}
import json
{% endif -%}
from pathlib import Path

# Add your imports here; numpy is only used as an example
import numpy as np


{% if cookiecutter.container_type == 'evaluation' -%}
def my_evaluation(submission_file, test_gt_file, out_file):
    with open(submission_file, 'r') as subm:
        submission_labels = np.loadtxt(subm)
    with open(test_gt_file, 'r') as gt:
        gt_labels = np.loadtxt(gt)

    num_correct = 0
    for subm_label, gt_label in zip(submission_labels, gt_labels):
        if subm_label == gt_label:
            num_correct += 1

    output = {'metrics': {'accuracy': float(num_correct)/len(gt_labels)}}

    with open(out_file, 'w') as f:
        json.dump(output, f)
{% else -%}
def my_submission(test_file, out_file):
    with open(test_file, 'r') as test:
        data = np.loadtxt(test)

    with open(out_file, 'w') as f:
        for sample in data:
            f.write(str(int(sample % 2)))
            f.write('\n')
{%- endif %}


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python src/{{ cookiecutter.container_type }}.py

    # These are the default file paths (names) for input and output, so don't
    # change them.
{%- if cookiecutter.container_type == 'evaluation' %}
    submission_file = str(Path('data')/'input'/'implementation_output')
    test_gt_file = str(Path('data')/'input'/'ground_truth')
    out_file = str(Path('data')/'output')

    my_evaluation(submission_file, test_gt_file, out_file)
{%- else %}
    test_file = str(Path('data')/'input'/'test_data')
    out_file = str(Path('data')/'output')

    my_submission(test_file, out_file)
{%- endif %}
