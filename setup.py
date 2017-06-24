from setuptools import setup

with open("requirements.txt", "r") as reqs:
    requirements = reqs.readlines()

setup(name='rcfc',
      version='0.2.3',
      description='A framework that gives a remote control for computers that is Python driven',
      url='http://github.com/pviafore/rcfc',
      author='Pat Viafore',
      author_email='patviafore+rcfc@gmail.com',
      license='MIT',
      packages=['rcfc'],
      install_requires=requirements,
      zip_safe=False)
