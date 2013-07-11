"""
    Forked from original Vizzuality code to use geventhttpclient

    Contributors: Javier Cordero <jneight@gmail.com>

    Original repo: https://github.com/Vizzuality/cartodb-python
"""

from setuptools import setup, find_packages


REQUIRES = ['oauth2', 'gevent', 'ujson']

setup(name='cartodb-geventhttpclient',
      author='Javier Cordero',
      author_email='jcorderomartinez@gmail.com',
      description='client to access cartodb api using geventhttpclient',
      version='0.6.3-gevent',
      url='https://github.com/yoinup/cartodb-python',
      install_requires=REQUIRES,
      packages=find_packages(),
      test_suite='cartodb.tests',)
