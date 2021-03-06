# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import esmtools

sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

current_year = datetime.datetime.now().year
project = 'esmtools'
copyright = f'2019-{current_year}, Riley X. Brady'
author = 'Riley X. Brady'

# The full version, including alpha/beta/rc tags
version = esmtools.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.napoleon',
    'sphinx.ext.imgmath',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.viewcode',
]

extlinks = {
    'issue': ('https://github.com/bradyrx/esmtools/issues/%s', 'GH#'),
    'pr': ('https://github.com/bradyrx/esmtools/pull/%s', 'GH#'),
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'
source_suffix = '.rst'
master_doc = 'index'
nbsphinx_timeout = 60

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = 'images/esmtools-logo.png'
html_theme_options = {'logo_only': True, 'style_nav_header_background': '#fcfcfc'}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    # 'xarray': ('https://http://xarray.pydata.org/en/stable/', None),
    # 'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    # 'iris': ('http://scitools.org.uk/iris/docs/latest/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    # 'numba': ('https://numba.pydata.org/numba-doc/latest/', None),
    # 'matplotlib': ('https://matplotlib.org/', None),
}
