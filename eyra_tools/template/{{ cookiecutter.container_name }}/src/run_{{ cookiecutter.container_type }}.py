from pathlib import Path

from {{ cookiecutter.container_type }} import my_{{ cookiecutter.container_type }}

class {{cookiecutter.container_type.capitalize()}}(object):
{% if cookiecutter.container_type == 'evaluation' %}
    def run(self, submission_file, test_gt_file, out_file):
{% else%}
    def run(self, test_file, out_file):
{% endif %}
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        ({{ cookiecutter.container_type.capitalize() }}) or the method name (run).
        """
    {%- if cookiecutter.container_type == 'evaluation' %}
        my_evaluation(submission_file, test_gt_file, out_file)
    {%- else%}
        my_submission(test_file, out_file)
    {%- endif %}


# Please do not change anything below
if __name__ == "__main__":
    # These are the default file paths (names) for input and output
{% if cookiecutter.container_type == 'evaluation' %}
    submission_file = Path('/')/'data'/'input'/'implementation_output'
    test_gt_file = Path('/')/'data'/'input'/'ground_truth'
    out_file = Path('/')/'data'/'output'

    Evaluation().run(submission_file, test_gt_file, out_file)
{% else %}
    # These are the default file paths (names) for input and output
    test_file = Path('/')/'data'/'input'/'test_data'
    out_file = Path('/')/'data'/'output'

    Submission().run(test_file, out_file)
{% endif %}
