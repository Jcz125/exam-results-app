from setuptools import setup

setup(
    name='yourscript',
    version='0.1',
    py_modules=['import_files'],
    install_requires=[
        'Click',
        'openpyxl',
        'pandas'
    ],
    entry_points='''
        [console_scripts]
        importxl=import_files:cli
    ''',
)
