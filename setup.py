from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='${version}',
    description='Blog System base on Django',
    author='sanlozhang',
    author_email='940072028@qq.com',
    url='https://github/com/sanlo',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    # package_data={'': ['themes/*/*/*/*']},
    include_package_data=True,
    install_requires=[
        'Django == 3.2.7',
        'django-debug-toolbar == 3.2.2',
        'django-simpleui == 2021.8.17',
        'djangorestframework == 3.12.4',
        'mysqlclient~=2.0',
        'gunicorn~=20.1',
        'supervisor~=4.2',
        'fabric == 2.6.0',
        'mistune == 0.8.4',
        'paramiko == 2.7.2',
        'pathlib2 == 2.3.6',
        'pycodestyle == 2.7.0',
        'pycparser == 2.20',
        'PyNaCl == 1.4.0',
        'pytz == 2021.1',
        'requests == 2.26.0',
        'sqlparse == 0.4.1',
        'toml == 0.10.2',
        'uritemplate == 3.0.1',
        'urllib3 == 1.26.6',

    ],
    extras_require={
        'ipython': ['ipython==7.27.0']
    },
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ]
)
