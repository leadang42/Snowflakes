from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="1.0.0",
    author="Lea Dang",
    author_email="leadang2001@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)