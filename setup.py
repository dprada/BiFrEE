"""
BiFrEE.
Binding Free Energy Estimator
"""
import sys
from setuptools import setup, find_packages
from numpy.distutils.core import setup
from numpy.distutils.extension import Extension
import versioneer

short_description = __doc__.split("\n")

# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:])


setup(
    name='bifree',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    package_dir={'bifree': 'bifree'},
    packages=find_packages(),
    include_package_data=True,
    package_data={'bifree': ['data']},
    scripts=[],
    setup_requires=[] + pytest_runner,
    platforms=['Linux',
                'Mac OS-X',
                'Unix',
                'Windows',
    ],
    python_requires=">=3.7",
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/BiFrEE',
    license='MIT',
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
)

