from distutils.core import setup

long_desc = open('README.md').read()

setup(
    name                = 'ndim',
    version             = '0.1',
    py_modules          = ['ndim'],
    description         = 'Utility functions for strings of binary digits',
    author              = 'David McEwan',
    author_email        = '',
    license             = 'GLPv3',
    platforms           = 'Python >2.6 including 3.x (OS Independent)',
    url                 = 'https://github.com/DavidMcEwan/ndim',
    
    classifiers         = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
                          ],
    
    long_description    = long_desc
)
