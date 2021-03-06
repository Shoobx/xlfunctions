import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


TESTS_REQUIRE = [
    'coverage',
    'flake8',
    'mock',
    'pytest',
]


setup(
    name="xlfunctions",
    version="0.1.0dev",
    author="Bradley van Ree",
    author_email="brads@bradbase.net",
    description=(
        "Implemententation of Python equivalents of MS Excel functions."
    ),
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
        ),
    url="https://github.com/bradbase/xlfunctions",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    install_requires=[
        'numpy >= 1.18.1',
        'pandas >= 1.0.1',
        'numpy_financial >= 1.0.0',
        'python-dateutil',
        'yearfrac',
    ],
    extras_require=dict(
        test=TESTS_REQUIRE,
    ),
    python_requires='>=3.7.6',
    tests_require=TESTS_REQUIRE,
)
