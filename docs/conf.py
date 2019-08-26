# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import os
import tempfile
import shutil

from pathlib import Path

from cookiecutter.main import cookiecutter

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
here = os.path.dirname(__file__)


# -- Project information -----------------------------------------------------

project = 'EYRA Tools'
copyright = '2019, EYRA Benchmark Team'
author = 'EYRA Benchmark Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon',
              'sphinx.ext.autosectionlabel', 'sphinx.ext.todo']

autosectionlabel_prefix_document = True
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Specify index.rst is the root of the documentation
# See https://stackoverflow.com/questions/56336234/build-fail-sphinx-error-contents-rst-not-found
master_doc = 'index'

def generate_code_examples(_):

    generate_project('submission')


def generate_project(container_type):
    """Generate the Python files using the cookiecutter and copy them to the
    documentation.
    """

    tmp_dir = tempfile.mkdtemp()

    template_dir = Path(__file__).parent.parent / "eyra_tools" / "template"

    cookiecutter(
        template=str(template_dir.absolute()),
        output_dir=tmp_dir,
        no_input=True,
        extra_context={
            "container_name": "test",
            "container_type": container_type
        },
    )

    src = Path(tmp_dir) / "test" / "algorithm_src" / "algorithm.py"
    dst = Path(here) / "algorithm.py"
    print('From:', src)
    print('To:', dst)
    shutil.copy(src, dst)

    shutil.rmtree(tmp_dir)


def setup(app):
    app.connect('builder-inited', generate_code_examples)
