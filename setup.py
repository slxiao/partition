"""partition: Python number partition algorithm library
"""
import io
from setuptools import setup


version = "0.1.2"

setup(
    include_package_data=True,
    name='partition',
    version=version,
    packages=['partition'],
    entry_points={
        'console_scripts': [
            'partition = partition.partition:partition',
        ]
    },
    url='https://github.com/slxiao/partition',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    license='MIT',
    author='slxiao',
    long_description=io.open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    author_email='shliangxiao@gmail.com',
    description='Python number partition algorithm library',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)