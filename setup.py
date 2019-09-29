from setuptools import setup


def fetch_version():
      '''
      Fetches version variable from version.py
      '''
      version = {}

      with open('dummysite/version.py') as f:
            exec(f.read(), version)

      return version['__version__']



setup(name='dummysite',
      version=fetch_version(),
      description='Sets up dummy website locally',
      url='http://github.com/UCLeuvenLimburg/dummysite',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['dummysite'],
      scripts = [ 'bin/dummysite' ],
      install_requires=['flask'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)