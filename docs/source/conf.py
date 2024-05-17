# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'metarepo'
copyright = '2024, Em Rexer, Chris Vernon'
author = 'Em Rexer, Chris Vernon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_theme_options = {
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': True,
    "nav_links": [
        {
            "title": "Use the `metarepo` template",
            "url": "https://github.com/new?template_name=metarepo&template_owner=IMMM-SFA"
        },
    ],
    "logo_target": "https://im3.pnnl.gov/",
}
html_logo = "_static/im3logo.png"
html_static_path = ['_static']
