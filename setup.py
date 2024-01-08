from setuptools import setup, find_packages

setup(
    name="kredivo-android-generator",
    version = "1.0.0",
    author = "Michael Kojansow",
    author_email = "michael.kojansow@finaccel.co",
    packages = find_packages(include = ['main', 'main.*']),
    entry_points = {
        'console_scripts': [
            'kredigen=main.generator:generate'
        ]
    }
)