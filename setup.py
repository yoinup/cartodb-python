"""
    Forked from original Vizzuality code to use geventhttpclient

    Contributors: Javier Cordero <jneight@gmail.com>

    Original repo: https://github.com/Vizzuality/cartodb-python
"""

#from distutils.core import setup
from setuptools import setup

REQUIRES = ['oauth2', 'gevent', 'ujson']

setup(name='cartodb',
      author='Javi Santana',
      author_email='jsantana@vizzuality.com',
      description='client to access cartodb api using geventhttpclient',
      version='0.6-gevent',
      url='https://github.com/yoinup/cartodb-python',
      install_requires=REQUIRES,
      packages=['cartodb'],
      requires=REQUIRES,
      test_suite='test.client')
