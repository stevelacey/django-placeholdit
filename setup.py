try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-placeholdit',
    version='1.0.1',
    description='A fully featured drop-in replacement of placehold.it for Django',
    long_description=open('README.rst').read(),
    keywords='django placeholder placehold.it',
    license=open('LICENSE').read(),
    author='Steve Lacey',
    author_email='steve@stevelacey.net',
    url='https://github.com/stevelacey/django-placeholdit',
    packages=['django_placeholdit'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ]
)
