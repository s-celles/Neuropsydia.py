from setuptools import setup, find_packages

setup(
name = "neuropsydia",
description = ("A Python module for creating experiments, tasks and questionnaires."),
version = "1.0.0",
license = "Mozilla Public License Version 2.0",
author = "Dominique Makowski",
author_email = "dom.makowski@gmail.com",
maintainer = "Dominique Makowski",
maintainer_email = "dom.makowski@gmail.com",
packages = find_packages(),
package_data = {
	"neuropsydia.files.font":["*.ttf"],
	"neuropsydia.files.binary":["*.png"],
	"neuropsydia.files.logo":["*.png"]},
install_requires = [
    'pygame>=1.9.2a0',
    'numpy>=1.11.0',
    'scipy>=0.10.0',
    'pandas>=0.18.0',
    'Pillow>=3.0.0',
    'plotly>=1.12.9',
    'cryptography>=1.5.2',
    'python-docx>=0.8.6',
    'pyxid>=1.0.0',
    'neurotools'],
dependency_links=['https://github.com/cedrus-opensource/pyxid/tarball/master#egg=pyxid',
                  'https://github.com/neuropsychology/NeuroTools.py/tarball/master#egg=neurotools'],
long_description = open('README.rst').read(),
keywords = "python neuropsychology neuropsydia experiment creation",
url = "https://github.com/neuropsychology/Neuropsydia.py/",
download_url = 'https://github.com/neuropsychology/Neuropsydia.py/tarball/1.0.0',
test_suite='nose.collector',
tests_require=['nose'],
classifiers = [
	'Intended Audience :: Science/Research',
	'Intended Audience :: Developers',
	'Programming Language :: Python',
	'Topic :: Software Development',
	'Topic :: Scientific/Engineering',
	'Operating System :: Microsoft :: Windows',
	'Operating System :: Unix',
	'Operating System :: MacOS',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6']
)
