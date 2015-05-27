from setuptools import setup, find_packages
setup(name='yam.backend',
			version='0.1.1',
			description="Shared python code for backend servers",
			long_description="Shared python code for backend servers",
			author="Dave Quigley",
			author_email="yam@davequigley.com",
			packages=find_packages(exclude="tests"))

