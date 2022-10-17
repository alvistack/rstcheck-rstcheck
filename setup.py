# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rstcheck']

package_data = \
{'': ['*']}

modules = \
['AUTHORS']
install_requires = \
['docutils>=0.7,<0.19',
 'pydantic>=1.2,<2.0',
 'rstcheck-core>=1.0.2,<2.0.0',
 'typer[all]>=0.3.2,<0.5',
 'types-docutils>=0.18,<0.19']

entry_points = \
{'console_scripts': ['rstcheck = rstcheck._cli:main']}

setup_kwargs = {
    'name': 'rstcheck',
    'version': '6.0.0.post1',
    'description': 'Checks syntax of reStructuredText and code blocks nested within it',
    'long_description': "========\nrstcheck\n========\n\n+-------------------+---------------------------------------------------------------------------------------------+\n| **General**       | |maintenance_y| |license| |semver|                                                          |\n|                   +---------------------------------------------------------------------------------------------+\n|                   | |rtd|                                                                                       |\n+-------------------+---------------------------------------------------------------------------------------------+\n| **CI**            | |gha_tests| |gha_docu| |gha_qa|                                                             |\n+-------------------+---------------------------------------------------------------------------------------------+\n| **PyPI**          | |pypi_release| |pypi_py_versions| |pypi_implementations|                                    |\n|                   +---------------------------------------------------------------------------------------------+\n|                   | |pypi_format| |pypi_downloads|                                                              |\n+-------------------+---------------------------------------------------------------------------------------------+\n| **Github**        | |gh_tag| |gh_last_commit|                                                                   |\n|                   +---------------------------------------------------------------------------------------------+\n|                   | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                                       |\n+-------------------+---------------------------------------------------------------------------------------------+\n\n\nChecks syntax of reStructuredText and code blocks nested within it.\n\nSee the full documentation at `read-the-docs`_\n\n\n.. contents::\n\n\nInstallation\n============\n\nFrom pip\n\n.. code:: shell\n\n    $ pip install rstcheck\n\nTo use pyproject.toml for configuration::\n\n    $ pip install rstcheck[toml]\n\nTo add sphinx support::\n\n    $ pip install rstcheck[sphinx]\n\n\nSupported languages in code blocks\n==================================\n\n- Bash\n- Doctest\n- C (C99)\n- C++ (C++11)\n- JSON\n- XML\n- Python\n- reStructuredText\n\n\nExamples\n========\n\n.. rstcheck: ignore-languages=cpp,python,rst\n\nWith bad Python syntax:\n\n.. code:: rst\n\n    ====\n    Test\n    ====\n\n    .. code:: python\n\n        print(\n\n.. code:: text\n\n    $ rstcheck bad_python.rst\n    bad_python.rst:7: (ERROR/3) (python) unexpected EOF while parsing\n\nWith bad C++ syntax:\n\n.. code:: rst\n\n    ====\n    Test\n    ====\n\n    .. code:: cpp\n\n        int main()\n        {\n            return x;\n        }\n\n.. code:: text\n\n    $ rstcheck bad_cpp.rst\n    bad_cpp.rst:9: (ERROR/3) (cpp) error: 'x' was not declared in this scope\n\nWith bad syntax in the reStructuredText document itself:\n\n.. code:: rst\n\n    ====\n    Test\n    ===\n\n.. code:: text\n\n    $ rstcheck bad_rst.rst\n    bad_rst.rst:1: (SEVERE/4) Title overline & underline mismatch.\n\n\n.. _read-the-docs: https://rstcheck.readthedocs.io\n\n\n.. General\n\n.. |maintenance_n| image:: https://img.shields.io/badge/Maintenance%20Intended-✖-red.svg?style=flat-square\n    :target: http://unmaintained.tech/\n    :alt: Maintenance - not intended\n\n.. |maintenance_y| image:: https://img.shields.io/badge/Maintenance%20Intended-✔-green.svg?style=flat-square\n    :target: http://unmaintained.tech/\n    :alt: Maintenance - intended\n\n.. |license| image:: https://img.shields.io/github/license/rstcheck/rstcheck.svg?style=flat-square&label=License\n    :target: https://github.com/rstcheck/rstcheck/blob/main/LICENSE\n    :alt: License\n\n.. |semver| image:: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square\n    :target: https://semver.org/\n    :alt: Semantic Versioning - 2.0.0\n\n.. |rtd| image:: https://img.shields.io/readthedocs/rstcheck/latest.svg?style=flat-square&logo=read-the-docs&logoColor=white&label=Read%20the%20Docs\n    :target: https://rstcheck.readthedocs.io/en/latest/\n    :alt: Read the Docs - Build Status (latest)\n\n\n.. CI\n\n\n.. |gha_tests| image:: https://img.shields.io/github/workflow/status/rstcheck/rstcheck/Test%20code/main?style=flat-square&logo=github&label=Test%20code\n    :target: https://github.com/rstcheck/rstcheck/actions/workflows/test.yaml\n    :alt: Test status\n\n.. |gha_docu| image:: https://img.shields.io/github/workflow/status/rstcheck/rstcheck/Test%20documentation/main?style=flat-square&logo=github&label=Test%20documentation\n    :target: https://github.com/rstcheck/rstcheck/actions/workflows/documentation.yaml\n    :alt: Documentation status\n\n.. |gha_qa| image:: https://img.shields.io/github/workflow/status/rstcheck/rstcheck/QA/main?style=flat-square&logo=github&label=QA\n    :target: https://github.com/rstcheck/rstcheck/actions/workflows/qa.yaml\n    :alt: QA status\n\n\n.. PyPI\n\n.. |pypi_release| image:: https://img.shields.io/pypi/v/rstcheck.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :target: https://pypi.org/project/rstcheck/\n    :alt: PyPI - Package latest release\n\n.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/rstcheck.svg?style=flat-square&logo=python&logoColor=FBE072\n    :target: https://pypi.org/project/rstcheck/\n    :alt: PyPI - Supported Python Versions\n\n.. |pypi_implementations| image:: https://img.shields.io/pypi/implementation/rstcheck.svg?style=flat-square&logo=python&logoColor=FBE072\n    :target: https://pypi.org/project/rstcheck/\n    :alt: PyPI - Supported Implementations\n\n.. |pypi_format| image:: https://img.shields.io/pypi/format/rstcheck.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :target: https://pypi.org/project/rstcheck/\n    :alt: PyPI - Format\n\n.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/rstcheck.svg?style=flat-square&logo=pypi&logoColor=FBE072\n    :target: https://pypi.org/project/rstcheck/\n    :alt: PyPI - Monthly downloads\n\n\n\n.. GitHub\n\n.. |gh_tag| image:: https://img.shields.io/github/v/tag/rstcheck/rstcheck.svg?sort=semver&style=flat-square&logo=github\n    :target: https://github.com/rstcheck/rstcheck/tags\n    :alt: Github - Latest Release\n\n.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/rstcheck/rstcheck.svg?style=flat-square&logo=github\n    :target: https://github.com/rstcheck/rstcheck/commits/main\n    :alt: GitHub - Last Commit\n\n.. |gh_stars| image:: https://img.shields.io/github/stars/rstcheck/rstcheck.svg?style=flat-square&logo=github\n    :target: https://github.com/rstcheck/rstcheck/stargazers\n    :alt: Github - Stars\n\n.. |gh_forks| image:: https://img.shields.io/github/forks/rstcheck/rstcheck.svg?style=flat-square&logo=github\n    :target: https://github.com/rstcheck/rstcheck/network/members\n    :alt: Github - Forks\n\n.. |gh_contributors| image:: https://img.shields.io/github/contributors/rstcheck/rstcheck.svg?style=flat-square&logo=github\n    :target: https://github.com/rstcheck/rstcheck/graphs/contributors\n    :alt: Github - Contributors\n\n.. |gh_watchers| image:: https://img.shields.io/github/watchers/rstcheck/rstcheck.svg?style=flat-square&logo=github\n    :target: https://github.com/rstcheck/rstcheck/watchers/\n    :alt: Github - Watchers\n",
    'author': 'Steven Myint',
    'author_email': 'git@stevenmyint.com',
    'maintainer': 'Christian Riedel',
    'maintainer_email': 'cielquan@protonmail.com',
    'url': 'https://github.com/rstcheck/rstcheck',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
