from setuptools import setup, find_packages

setup(
    name="kredivo-android-generator",
    version = "1.0.0",
    author = "Michael Kojansow",
    author_email = "michael.kojansow@finaccel.co",
    packages = find_packages(include = ['kredivo_generator', 'kredivo_generator.*']),
    entry_points = {
        'console_scripts': [
            'kredigen=kredivo_generator.generator:generate'
        ]
    }
)