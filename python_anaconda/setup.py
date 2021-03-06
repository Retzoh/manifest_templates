"""Install pip dependencies & the package {PACKAGE_NAME}

See test/test_import.py for an import example
"""

from setuptools import setup, find_packages

# The name with which pip references the package (for updates/uninstall)
PACKAGE_NAME = "python-example"

# PACKAGE_PATH should match the name of your python module inside "src"
PACKAGE_PATH = PACKAGE_NAME.replace('-', '_')

setup_params = dict(
    name=PACKAGE_NAME,

    # pip dependencies declaration
    tests_require=[
        "pytest==4.4.*",
        "pytest-cov==2.7.*",
    ],
    install_requires=[
        "setuptools==41.0.*",
    ],

    # Tell where the source code for the package is located
    package_dir={"": "src"},
    packages=find_packages("src", include=[PACKAGE_PATH, PACKAGE_PATH + ".*"]),
    include_package_data=True,
)

setup(**setup_params)
