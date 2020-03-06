import os
from setuptools import setup,find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "Broadworks Django Authentication",
    version = "0.0.1",
    author = "Aaron Parfitt",
    author_email = "aaronparfitt123@gmail.com",
    description = ("Broadworks Authentication for your django app"),
    keywords = ["Broadworks", "Django"],
    packages=find_packages(),
    install_requires = ['BroadworksOCIP',],
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    classifiers=[
        "Framework :: Django :: 2.1",
        "Development Status :: 3 - Alpha",
    ],
)