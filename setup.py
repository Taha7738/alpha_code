from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alpha_code/__init__.py
from alpha_code import __version__ as version

setup(
	name="alpha_code",
	version=version,
	description="alpha code",
	author="alpha code",
	author_email="alphaCode@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
