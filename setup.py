import os
import sys
import dailyrotatingfilehandler

if sys.argv[-1] == 'publish':
    os.system("del /Q dist\\*")
    os.system("python setup.py bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

from setuptools import setup

#Get version
version = dailyrotatingfilehandler.__version__

#Get long description.
long_description = ""
with open("README.rst") as f:
    long_description = f.read()

setup(name = 'dailyrotatingfilehandler',
    version = version,
    url = 'https://github.com/borisliu/daily-rotating-file-handler',
    license = 'MIT',
    author = 'borisliu',
    author_email = 'boris_cn@263.net',
    description = 'Rotating the log file every midnight.',
    long_description = long_description,
    platforms=['all'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=['dailyrotatingfilehandler'],
)