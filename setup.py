##used for building our app as a package which can be used in other codes

from setuptools import find_packages,setup

setup(
  name='mlproject',
  version='0.0.1',
  author='Asra',
  author_email='asrajamalashraf@gmail.com',
  packages=find_packages(),
  install_requires=['pandas', 'numpy', 'seaborn']
)