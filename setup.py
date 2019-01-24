from setuptools import setup
from parallelforeachsubmodule.metadata import Metadata

metadata = Metadata()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """"
pySimpleHTTPDownloader
--------------------------
Simple HTTP downloader written in Python
    """


setup(
    name = 'simple_http_downloader',
    packages = ['pysimplehttpdownloader'],
    install_requires = requirements(),
    version = metadata.get_version(),
    license = 'LGPL v3',
    description = 'Simple HTTP downloader written in Python',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/pySimpleHTTPDownloader',
    download_url = 'https://github.com/RDCH106/pySimpleHTTPDownloader/archive/v'+metadata.get_version()+'.tar.gz',
    #entry_points={
    #    'console_scripts': ['pfs=pysimplehttpdownloader.main:main'],
    #},
    keywords = 'http downloader',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)