from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read().replace('.. :changelog:', '')

setup(
    name='sqlalchemy-redshift',
    version='0.7.3.1',
    description='Amazon Redshift Dialect for sqlalchemy',
    long_description=readme + '\n\n' + history,
    author='Matt George',
    author_email='mgeorge@gmail.com',
    maintainer='Thomas Grainger',
    maintainer_email='sqlalchemy-redshift@graingert.co.uk',
    license="MIT",
    url='https://github.com/sqlalchemy-redshift/sqlalchemy-redshift',
    packages=['sqlalchemy_redshift', 'redshift_sqlalchemy'],
    package_data={'sqlalchemy_redshift': ['redshift-ca-bundle.crt']},
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'psycopg2-binary>=2.5',
         # requires sqlalchemy.sql.base.DialectKWArgs.dialect_options, new in
         # version 0.9.2
        'SQLAlchemy>=0.9.2,<2.0.0',
    ],
    extras_require={
        ':python_version < "3.4"': 'enum34 >= 1.1.6, < 2.0.0'
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        'sqlalchemy.dialects': [
            'redshift = sqlalchemy_redshift.dialect:RedshiftDialect',
            'redshift.psycopg2 = sqlalchemy_redshift.dialect:RedshiftDialect',
        ]
    },
)
