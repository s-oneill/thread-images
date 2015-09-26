try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'image downloader',
    'author': 'Shane ONeill',
    'url': 'https://github.com/shoneill/thread-images',
    'download_url': 'https://github.com/shoneill/thread-images',
    'author_email': 'oneill.shane.h@gmail.com',
    'version': '1.0',
    'scripts'=['bin/thread-images'],
    'packages': ['thread-images'],
    'name': 'thread-images'
}

setup(**config)
