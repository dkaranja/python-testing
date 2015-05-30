from setuptools import setup

name = 'merge_sort'
version = '1.0.0'

setup(
    name=name,
    version=version,
    packages=[

    ],
    description="Merge sort algorithm",
    author="Denis Karanja",
    author_email="denis.karanja@savannahinformatics.com",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Everyone',
        'Topic :: Software Testing :: Algorithms',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'tox',
    ]
)