Best Practices
--------------

Some best practices for creating submissions and evaluation containers.

Put your code under version control
###################################

After you generated a submission or evaluation project, put it under version control!
If you are using git, you can so by typing:

.. code-block:: sh

    git init
    git add -A
    git commit -m "Initial commit"

And put it on `GitHub <https://guides.github.com/activities/hello-world/>`_.

Put the complicated parts of your algorithm in a separate Python package
########################################################################

Although all code and other files that are put inside the ``src`` directory are
copied to the container, once your code gets complicated, it might be a better
idea to create a separate Python package for your code, install it inside the
container and call the required functionality from ``src/run_submission.py`` or
``run_evaluation.py``.

Have a look at the `section on building and packaging Python code
<https://guide.esciencecenter.nl/best_practices/language_guides/python.html#building-and-packaging-code>`_
in the Netherlands eScience Center Software Development guide
to get pointers on how to create a Python package.

Use semantic versioning for your Docker tags
############################################

Using `semantic versioned <https://semver.org>`_ Docker tags helps you and
others to keep track of what you did.
If you use the ``latest`` tag for your submission or evaluation, the
EYRA Benchmark Platform might fail to use the latest version.

Start with version 0.1.0.

Add an Open Source license to your code
#######################################

Having a license on your code allows others to inspect and (re-)use your code.
This is essential to reproducibility, peer-review, and the ability to
build upon others' work. Do you need more information about software licenses
and/or advice on what license to choose? Have a look at these blog posts:

* `A license to science
  <https://blog.esciencecenter.nl/a-license-to-science-cd8030a4a145>`_
  by Lourens Veen
* `A Data Scientist's Guide to Open Source Licensing
  <https://towardsdatascience.com/a-data-scientists-guide-to-open-source-licensing-c70d5fe42079>`_
  by mattymecks
