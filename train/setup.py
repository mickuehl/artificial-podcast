"""Artificial Podcast Trainer configuration."""
from setuptools import find_packages
from setuptools import setup

# see https://cloud.google.com/ai-platform/training/docs/runtime-version-list

REQUIRED_PACKAGES = [
      'requests == 2.25.1',
      'setuptools',
      'tensorflow == 2.4.*',
      'tensorflow_datasets',
      'sklearn',
      'datasets >= 1.8.0',
      'torch >= 1.8',
      'sentencepiece > 0.1.92',
      'transformers == 4.8.*'
      ]
      
setup(
      name='train.art-podcast',
      version='1.0',
      install_requires=REQUIRED_PACKAGES,
      packages=find_packages(),
      include_package_data=True,
      description='Artificial Podcast Trainer'
)