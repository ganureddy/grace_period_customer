from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in grace_period_customer/__init__.py
from grace_period_customer import __version__ as version

setup(
	name="grace_period_customer",
	version=version,
	description="Grace Period Customer",
	author="Ganu Reddy",
	author_email="ganur379@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
