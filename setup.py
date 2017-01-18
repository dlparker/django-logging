import os
import re
from setuptools import setup, find_packages


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        return readme.read()


def version():
    #pattern = re.compile(r'__version__ = \'([\d\.]+)\'')
    with open(os.path.join('django_logging_dlp', '__init__.py')) as f:
        data = f.read()
        target = '__version__ = '
        index = data.index(target)
        index += len(target)
        value = data[index:].split()[0]
        return value


setup(
    name='django-logging-json-dlp',
    version=version(),
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description='A simple Django app to log requests/responses in various formats, such as JSON. Fork of https://github.com/cipriantarta/django-logging with added controls for user.',
    long_description=readme(),
    url='https://github.com/dlparker/django-logging',
    author='Ciprian Tarta, Dennis Parker',
    author_email='me@cipriantarta.ro, dennis@windhavengroup.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Framework :: Django",
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
    ],
    keywords='django logging json',
    install_requires=[
        'django>=1.4',
        'six',
        'elasticsearch>=2.0.0,<3.0.0',
    ]
)
