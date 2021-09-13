from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='0.2',
    description='Blog System base on Django',
    author='sanlozhang',
    author_email='940072028@qq.com',
    url='https://github/com/sanlo',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': ['themes/*/*/*/*']},
    install_requires=[
        'django~=3.2',
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        'mysqlclient==1.3.12',
        'django-rest-framework==0.1.0',
        'django-redis==4.8.0',
        'mistune==0.8.3',
        'coreapi==2.3.3',
        # debug
        'django-debug-toolbar==1.9.1',
    ],
    extras_require={
        'ipython': ['ipython==7.27.0']
    },
    scripts=[
        'typeidea\manage.py',
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
