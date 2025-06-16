# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Manual de Identidad MxOS'
copyright = '2025, Fundación MxOS'
author = 'Fundación MxOS'
version = '0.1'
release = '0.1'
license = 'Creative Commons CC BY-SA 4.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_design', 'sphinx.ext.todo']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# Enable TODOs
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://pradyunsg.me/furo/customisation/

html_baseurl = 'https://mx-os.mx/'
html_favicon = 'assets/logo-principal.png'
html_logo = 'assets/logo-principal.png'

html_theme = 'furo'
html_static_path = ['_static']

# Furo customizations
html_title = 'MxOS'
html_theme_options = {
    'navigation_with_keys': True,
    'light_css_variables': {
        'font-stack': 'Metrophobic'
    },
    'dark_css_variables': {
        'color-background-primary': '#111',
        'color-background-secondary': '#111115'
    }
}

latex_theme = 'howto'


# pygments
pygments_style = 'sphinx'
pygments_dark_style = 'monokai'
