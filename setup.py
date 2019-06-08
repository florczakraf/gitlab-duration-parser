# -*- coding: utf-8 -*-
import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='gitlab-duration-parser',
    use_scm_version=True,
    author='Rafał Florczak',
    description='A simple Gitlab time-tracking message parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/florczakraf/gitlab-duration-parser',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
