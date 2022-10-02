# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Fast API'
copyright = 'Samuel Bailey'
author = 'Samuel Bailey'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "myst_parser",
    "sphinx_markdown_tables",
    "sphinx_tabs.tabs",
    "sphinxcontrib.httpdomain",
    "sphinxext.opengraph"
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_title = "Fast API"
html_theme_options = {
    "display_version": False,
    "prev_next_buttons_location": False,
    "sticky_navigation": False
}
html_css_files = [
    "/_static/custom.css?" + str(round(time.time())),
    "https://use.fontawesome.com/releases/v5.13.0/css/all.css"
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
