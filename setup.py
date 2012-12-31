"""
    Forked from original Vizzuality code to use geventhttpclient

    Contributors: Javier Cordero <jneight@gmail.com>

    Original repo: https://github.com/Vizzuality/cartodb-python
"""

from setuptools import setup, find_packages


REQUIRES = ['oauth2', 'gevent', 'ujson']

setup(name='cartodb',
      author='Javi Santana',
      author_email='jsantana@vizzuality.com',
      maintainer='Javier Cordero',
      maintainer_email='jcorderomartinez@gmail.com',
      description='client to access cartodb api using geventhttpclient',
      version='0.6-gevent',
      url='https://github.com/yoinup/cartodb-python',
      install_requires=REQUIRES,
      packages=find_packages(),
      requires=REQUIRES,
      test_suite='test.client')
