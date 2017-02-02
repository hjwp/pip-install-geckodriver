#!/usr/bin/env python

from distutils.core import setup
import sys

arch = '64' if sys.maxsize > 2**32 else '32'
if 'linux' in sys.platform:
    geckodriver = 'bin/linux/{arch}/geckodriver'.format(arch=arch)
elif 'win32' in sys.platform:
    geckodriver = 'bin/windows/{arch}/geckodriver.exe'.format(arch=arch)
elif 'darwin' in sys.platform:
    geckodriver = 'bin/osx/geckodriver'


setup(
    name='geckodriver',
    version='0.14.0',
    description='Pip-installable version of Geckodriver (the Firefox driver for Selenium)',
    author='Harry Percival',
    author_email='obeythetestinggoat@gmail.com',
    url='https://github.com/hjwp/pip-install-geckodriver',
    download_url='https://github.com/mozilla/geckodriver/tree/v0.14.0/dist/geckodriver.zip',
    packages=[],
    scripts=[geckodriver],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache',
    ],
)
