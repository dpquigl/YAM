from setuptools import setup, find_packages
setup(name='pyyamproto.protocol',
			version='0.1.1',
			description="Python protocol message classes generated from protocol buffers",
			long_description="Python protocol message classes generated from protocol buffers",
			author="Dave Quigley",
			author_email="yam@davequigley.com",
			packages=find_packages(exclude="tests"))

