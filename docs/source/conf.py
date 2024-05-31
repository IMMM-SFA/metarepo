# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'metarepo'
copyright = '2024, Integrated Multisector, Multiscale Modeling (IM3)'
author = 'Chris Vernon, Em Rexer'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.youtube'
    ]

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
            "title": "Use the metarepo template",
            "url": "https://github.com/new?template_name=metarepo&template_owner=IMMM-SFA",
        },
    ],
    "logo_target": "https://immm-sfa.github.io/metarepo",
}
html_logo = "metarepo_logo.png"
html_static_path = ['_static']
html_sidebars = {
    "**": [
        "sidebars/localtoc.html",
        "sidebars/repo-stats.html"
    ]
}
html_context = {
    "source_type": "github",
    "source_user": "IMMM-SFA",
    "source_repo": "metarepo",
}