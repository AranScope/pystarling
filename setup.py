from setuptools import setup

setup(name="starling",
      version="0.0.1",
      description="A python SDK for interacting with the Starling V1 API.",
      url="https://github.com/aranscope/starling-python-sdk",
      author="Aran Long",
      author_email="me@aran.site",
      license="MIT",
      packages=["starling"],
      install_requires=["requests"]
      )
