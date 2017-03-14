from setuptools import setup


setup(
    name='GPA_Calculator',
    version='0.9',
    author='Marc Frankel',
    packages=['GPA_Calculator'],
    entry_points={
          'console_scripts': [
              'GPA-Calculator = GPA_Calculator.__main__:main'
          ]
      },
    url='https://marcafrankel.com',
    license='MIT',
)