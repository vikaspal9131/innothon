from setuptools import setup, find_packages

setup(
    name='skitech-streamlit',
    version='1.0',
    packages=find_packages(include=['backend', 'tests']),
)
