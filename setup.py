from setuptools import setup, find_packages

setup(
    name='urban_cli',
    version='0.1.0',
    description='Command line for the Urban Dictionary',
    author='Joshua Rose',
    author_email='joshuarose099@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama',
        'typing_extensions',
        'lxml',
        'rich',
        'pytest',
        'pytest-cov',
        'coveralls',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Everyone',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
