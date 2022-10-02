import time

exclude_patterns = ["README.md"]

extensions = [
    "myst_parser",
    "sphinx_markdown_tables",
    "sphinx_tabs.tabs",
    "sphinxcontrib.httpdomain",
    "sphinxext.opengraph"
]

html_css_files = [
    "/_static/custom.css?" + str(round(time.time())),
    "https://use.fontawesome.com/releases/v5.13.0/css/all.css"
]
html_js_files = ["/_static/custom.js?" + str(round(time.time()))]
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": False,
    "prev_next_buttons_location": False,
    "sticky_navigation": False
}
html_title = "Fast API"

myst_heading_anchors = 6

project = "Fast API"
author = "Samuel Bailey"
