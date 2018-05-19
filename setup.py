from setuptools import setup

with open("requirements.txt", "r") as reqs:
    requirements = reqs.readlines()

setup(name='rcfc',
      version='1.0.0',
      description='A framework that gives a remote control for any Python function you want to run on a computer',
      url='http://github.com/pviafore/rcfc',
      author='Pat Viafore',
      author_email='patviafore+rcfc@gmail.com',
      license='MIT',
      packages=['rcfc'],
      package_data={'rcfc': ['static/*']},
      install_requires=requirements,
      python_requires='>=3.6',
      zip_safe=False,
      entry_points={
            'console_scripts': ['rcfc_demo = rcfc.demo:main']
      })
