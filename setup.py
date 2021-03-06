from setuptools import setup, find_packages

version = '0.6.4'

setup(name='Products.FirebirdDA',
      version=version,
      description="Firebird database adapter for Zope2",
      long_description=open("README.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Zope2",
        "License :: OSI Approved :: Zope Public License",
        ],
      keywords='Firebird',
      author='Hajime Nakagami',
      author_email='nakagami@gmail.com',
      url='https://github.com/nakagami/Products.FirebirdDA',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'firebirdsql',
          'ThreadLock',
          'Products.ZSQLMethods',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
