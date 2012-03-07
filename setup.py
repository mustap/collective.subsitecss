import os
from setuptools import setup, find_packages


setup(name='collective.subsitecss',
      version='0.1',
      description="edit css for subsites",
      long_description=open('README.txt').read(),
      keywords='',
      author='Mustapha Benali',
      author_email='mustapha@headnet.dk',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
)
