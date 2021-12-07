from setuptools import setup

setup(name='rancat',
      version='0.1',
      description='Random halo catalogs',
      url='http://github.com/marcelo-alvarez/rancat',
      author='Marcelo Alvarez',
      license='MIT',
      packages=['rancat'],
      package_dir={'rancat': 'rancat'},
      package_data={'rancat': ['*.dat']},
      zip_safe=False)
