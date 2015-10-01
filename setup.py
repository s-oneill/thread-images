try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import threadimages

config = {
    'description': 'image downloader',
    'author': 'Shane ONeill',
    'version': threadimages.__version__,
    'license': threadimages.__license__,
    'url': 'https://github.com/shoneill/thread-images',
    'download_url': 'https://github.com/shoneill/thread-images',
    'author_email': 'oneill.shane.h@gmail.com',
    'version': '1.0',
    'scripts':['bin/thread-images'],
    'packages': ['threadimages'],
    'name': 'thread-images'
}

setup(**config)
