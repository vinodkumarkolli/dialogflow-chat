# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dialogflow_chat/__init__.py
from dialogflow_chat import __version__ as version

setup(
	name='dialogflow_chat',
	version=version,
	description='Connects ERPNext Chat App with dialogflow Chatbot',
	author='Arrow Foods India Pvt Ltd',
	author_email='sreevinaayaka.traders@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
