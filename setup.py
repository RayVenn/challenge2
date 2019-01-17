from setuptools import setup, find_packages

setup(
    name='challenge2',
    version='0.0.1',
    description='challenge2',
    packages=find_packages(),
    entry_points={
          'console_scripts': [
              'find-pair = challenge2.find_pair:main'
          ]
      },
)
