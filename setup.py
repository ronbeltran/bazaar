from setuptools import setup

setup(name='bazaar',
      version='0.0.1',
      description='Random item and Heroku-ish name generator',
      url='https://github.com/ronbeltran/bazaar',
      author='Ronnie Beltran',
      author_email='rbbeltran.09@gmail.com',
      license='MIT',
      packages=['bazaar'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
