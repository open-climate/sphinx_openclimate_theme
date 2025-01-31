"""Sphinx openclimate Theme.
"""
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from os import path

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('openclimate', path.abspath(path.dirname(__file__)))
