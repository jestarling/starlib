from setuptools import setup, find_packages

setup(name='starlib',
      version='0.1',
      description='A package with some useful utility functions.',
      long_description='Learning Python package development.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='statistics',
      url='http://github.com/jestarling/starlib',
      author='Jennifer E Starling',
      author_email='jstarling@utexas.edu',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)