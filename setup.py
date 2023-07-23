from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bench_start/__init__.py
from bench_start import __version__ as version

setup(
	name="bench_start",
	version=version,
	description="run bench from another bench after login successfull",
	author="zubair",
	author_email="zubairmazhar23@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
