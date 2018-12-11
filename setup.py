import os

from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='python-cnab',
      version='1.0',
      description='Import file in the format cnab240',
      long_description=open(README).read(),
      author="codevance",
      author_email="contato@codevance.com.br",
      license="MIT",
      py_modules=['python-cnab'],
      zip_safe=False,
      platforms='any',
      tests_require=['pytest', 'pytest-coverage'],
      test_suite='tests',
      include_package_data=True,
      url='https://github.com/codevance/python-cnab', )
