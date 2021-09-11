from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='sanlozhang',
    author_email='940072028@qq.com',
    url='https://github/com/sanlo',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': ['themes/*/*/*/*']},
    install_requires=['django~=3.2', ],
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
