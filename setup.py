from setuptools import setup

setup(
    name='yourscript',
    version='0.1',
    py_modules=['test_module'],
    install_requires=[
        'Click',
        'openpyxl'
    ],
    entry_points='''
        [console_scripts]
        importxl=test_module:cli
    ''',
)