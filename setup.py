from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='holidays_calendar',
    version='1.0.0.0',
    description='Extends calendar.HTMLCalendar to allow holidays_calendar configuration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Arnaldo Ono',
    author_email='git@onoarnaldo.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='HTMLCalendar, development',
    package_dir={'': 'src', 'holidays_calendar': 'src/holidays_calendar'},
    packages=find_packages(where='src'),
    python_requires='>=3.9, <4',

    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },
)