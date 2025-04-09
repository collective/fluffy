# Configuration file for the Sphinx documentation builder.
# Fluffy build configuration file


# -- Path setup --------------------------------------------------------------

from datetime import datetime

from packaging.version import Version
from plone_sphinx_theme import __version__

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath("../src/plone_sphinx_theme"))

# -- Project information -----------------------------------------------------

project = "Fluffy"
author = "Plone Foundation"
trademark_name = "collective"
now = datetime.now()
year = str(now.year)
copyright = year


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = __version__
# The short X.Y version.
version = "v" + (Version(str(release)).base_version)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ""
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = "%B %d, %Y"


# -- General configuration ----------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named "sphinx.ext.*")
# or your custom ones.
extensions = [
    "myst_parser",
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",  # plone.api
    "sphinx.ext.doctest",  # plone.api
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",  # plone.api
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_examples",
    "sphinx_reredirects",
    "sphinx_sitemap",
    "sphinxcontrib.httpdomain",  # plone.restapi
    "sphinxcontrib.httpexample",  # plone.restapi
    "sphinxcontrib.mermaid",
    "sphinxcontrib.video",
    "sphinxcontrib.youtube",
    "sphinxext.opengraph",
]

# If true, the Docutils Smart Quotes transform, originally based on SmartyPants
# (limited to English) and currently applying to many languages, will be used
# to convert quotes and dashes to typographically correct entities.
smartquotes = False

# Options for the linkcheck builder
# Ignore localhost
linkcheck_ignore = [
    # Ignore local and example URLs
    r"http://0.0.0.0",
    r"http://127.0.0.1",
    r"http://localhost",
    # Ignore file downloads
    r"^/_static/",
    # Ignore pages that require authentication
    r"https://github.com/collective/fluffy/issues/new",  # requires auth
    # Ignore github.com pages with anchors
    r"https://github.com/.*#.*",
    # Ignore other specific anchors
]
linkcheck_allowed_redirects = {  # TODO: Confirm usage of linkcheck_allowed_redirects
    # All HTTP redirections from the source URI to the canonical URI will be treated as "working".
}
linkcheck_anchors = True
linkcheck_timeout = 5
linkcheck_retries = 1

# The suffix of source filenames.
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

suppress_warnings = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "plone_sphinx_theme"  # This can be configured
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"
# The default value includes icon-links, so override it with that one omitted, and add it to html_theme_options[footer_content_items].
html_sidebars = {
    "**": [
        "navbar-logo",
        "search-button-field",
        "sbt-sidebar-nav",
    ]
}
html_theme_options = {
    "article_header_start": ["toggle-primary-sidebar"],
    # "extra_footer": """<p>Example `extra_footer` content. License info. Trademark info and usage.</p>
    # <p>Pull request previews by <a href="https://readthedocs.org/">Read the Docs</a>.</p>""",
    "footer_content_items": [
        "author",
        "copyright",
        "last-updated",
        "extra-footer",
        "icon-links",
    ],
    # Uncomment for a page-wide footer
    # "footer_end": ["version.html"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/collective/fluffy",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
            "attributes": {
                "target": "_blank",
                "rel": "noopener me",
                "class": "nav-link custom-fancy-css",
            },
        },
        # {
        #   "name": "Mastodon",
        #   "url": "https://MY_MASTODON_SERVER/@MY_MASTODON_USER",
        #   "icon": "fa-brands fa-mastodon",
        #   "type": "fontawesome",
        #   "attributes": {
        #       "target": "_blank",
        #       "rel": "noopener me",
        #       "class": "nav-link custom-fancy-css",
        #    },
        # },
    ],
    "logo": {
        "text": "Fluffy",
    },
    "navigation_with_keys": True,
    "path_to_docs": "docs/docs",
    "repository_branch": "main",
    "repository_url": "https://github.com/collective/fluffy",
    "search_bar_text": "Search",
    "show_toc_level": 2,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
}
# suggest edit link
# remark:  is mandatory in "edit_page_url_template"
# html_context = {
#     "edit_page_url_template": "https://github.com/collective/fluffy/edit/main/docs/",
# }

# Announce that we have an opensearch plugin
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_use_opensearch
html_use_opensearch = "https://MY_READTHEDOCS_PROJECT_SLUG.readthedocs.io"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%(project)s v%(release)s" % {"project": project, "release": release}

# If false, no index is generated.
html_use_index = True

# html_css_files = ["custom.css", ("print.css", {"media": "print"})]
# html_js_files = []

html_extra_path = [
    "robots.txt",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    "_static",
]


# -- Options for autodoc ----------------------------------------------------

# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
# Automatically extract typehints when specified and place them in
# descriptions of the relevant function/method.
# autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "separated"


# -- Options for sphinx_sitemap to html -----------------------------

# Used by sphinx_sitemap to generate a sitemap
html_baseurl = "https://MY_READTHEDOCS_PROJECT_SLUG.readthedocs.io/"
# https://sphinx-sitemap.readthedocs.io/en/latest/advanced-configuration.html#customizing-the-url-scheme
sitemap_url_scheme = "{link}"
sitemap_filename = "sitemap-custom.xml"

# -- Options for myST markdown conversion to html -----------------------------

# For more information see:
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "attrs_block",  # Support parsing of block attributes.
    "attrs_inline",  # Support parsing of inline attributes.
    "colon_fence",  # You can also use ::: delimiters to denote code fences, instead of ```.
    "deflist",  # Support definition lists. https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    "html_image",  # For inline images. See https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#html-images
    "linkify",  # Identify "bare" web URLs and add hyperlinks.
    "strikethrough",  # See https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-strikethrough
    "substitution",  # Use Jinja2 for substitutions. https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
]

myst_substitutions = {}

# -- Intersphinx configuration ----------------------------------

# This extension can generate automatic links to the documentation of objects
# in other projects. Usage is simple: whenever Sphinx encounters a
# cross-reference that has no matching target in the current documentation set,
# it looks for targets in the documentation sets configured in
# intersphinx_mapping. A reference like :py:class:`zipfile.ZipFile` can then
# linkto the Python documentation for the ZipFile class, without you having to
# specify where it is located exactly.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}


# -- GraphViz configuration ----------------------------------
graphviz_output_format = "svg"


# -- Mermaid configuration ----------------------------------
mermaid_version = "11.2.0"


# -- OpenGraph configuration ----------------------------------
ogp_site_url = "https://MY_READTHEDOCS_PROJECT_SLUG.readthedocs.io/"
ogp_description_length = 200
ogp_image = "https://MY_READTHEDOCS_PROJECT_SLUG/_static/MY_LOGO.svg"
ogp_site_name = "Fluffy Documentation"
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta property="og:locale" content="en_US" />',
]


# -- sphinx.ext.todo -----------------------
# See http://sphinx-doc.org/ext/todo.html#confval-todo_include_todos
todo_include_todos = True


# -- sphinx-notfound-page configuration ----------------------------------
notfound_urls_prefix = ""
notfound_template = "404.html"


# -- sphinx-reredirects configuration ----------------------------------
# https://documatt.com/sphinx-reredirects/usage.html
redirects = {}


# -- Options for HTML help output -------------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "FluffyDocumentation"


# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
latex_documents = [
    (
        "index",
        "FluffyDocumentation.tex",
        "Fluffy Documentation",
        "collective community",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/logo.svg"


# --  Configuration for source_replacements extension -----------------------
# An extension that allows replacements for code blocks that
# are not supported in `rst_epilog` or other substitutions.
# https://stackoverflow.com/a/56328457/2214933
def source_replace(app, docname, source):
    result = source[0]
    for key in app.config.source_replacements:
        result = result.replace(key, app.config.source_replacements[key])
    source[0] = result


# Dict of replacements.
source_replacements = {
    "{SUPPORTED_PYTHON_VERSIONS}": "3.10, 3.11, 3.12, or 3.13",
}


# Finally, configure app attributes.
def setup(app):
    app.add_config_value("source_replacements", {}, True)
    app.connect("source-read", source_replace)
    # For sphinx.ext.ifconfig
    app.add_config_value("context", "documentation", "env")
