# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys
from sphinx.domains import Domain

sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))

import autogen

# This class translates tries to work around a bug in commonmark:
# commonmark removes the extension from all links ending in .md, even if
# they are not pointing to a local file built by sphinx
# See also this TODO in recommonmark.
# https://github.com/readthedocs/recommonmark/blob/ddd56e7717e9745f11300059e4268e204138a6b1/recommonmark/parser.py#L152-L155
# This class checks if a link is relative and then replaces the target
# with an URL built from the github URL and the link text
# That means we have to use the file extension in the link text for
# now

class GithubURLDomain(Domain):
    """
    Resolve certain links in markdown files to github source.
    """

    ROOT = "https://github.com/certtools/intelmq/blob/master/"

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        if contnode["refuri"].startswith("../"):
            print(f"Replacing {contnode['refuri']} with {self.ROOT}{contnode.rawsource}")
            contnode["refuri"] = self.ROOT + contnode.rawsource
            return [("githuburl:any", contnode)]
        else:
            return []

# -- Project information -----------------------------------------------------

project = 'intelmq'
copyright = '2020, cert.at'
author = 'IntelMQ Community'

# The full version, including alpha/beta/rc tags
release = '2.3.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.autodoc',
        'recommonmark',
        'sphinx_markdown_tables',
        'sphinx.ext.napoleon'
]

# Napoleon settings
# based on https://github.com/certtools/intelmq/issues/910
#napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
#napoleon_include_special_with_doc = True
#napoleon_use_admonition_for_examples = False
#napoleon_use_admonition_for_notes = False
#napoleon_use_admonition_for_references = False
#napoleon_use_ivar = False
#napoleon_use_param = True
#napoleon_use_rtype = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'source/intelmq.tests.*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
        'logo': 'Logo_Intel_MQ.svg',
        'github_user': 'certtools',
        'github_repo': 'intelmq',
        'font_family': "'Open Sans', sans-serif",
        'description': 'IntelMQ is a solution for IT security teams for collecting and processing security feeds using a message queuing protocol.'
        }

def run_apidoc(_):
    subprocess.check_call("sphinx-apidoc -o source ../intelmq", shell=True)


def run_autogen(_):
    with open('guides/Harmonization-fields.md', 'w') as handle:
        handle.write(autogen.harm_docs())
    with open('guides/Feeds.md', 'w') as handle:
        handle.write(autogen.feeds_docs())


def setup(app):
    app.add_domain(GithubURLDomain)
    app.connect("builder-inited", run_apidoc)
    app.connect("builder-inited", run_autogen)
