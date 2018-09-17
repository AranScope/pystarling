import setuptools
from setuptools import setup

setup(name="pystarling",
      version="0.0.5",
      description="A python SDK for interacting with the Starling V1 API.",
      url="https://github.com/aranscope/starling-python-sdk",
      author="Aran Long",
      author_email="me@aran.site",
      license="MIT",
      packages=setuptools.find_packages(exclude=["test"]),
      install_requires=["requests"],
      )
