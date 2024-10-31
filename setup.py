from setuptools import find_packages, setup


# exec() is a clever function that reads the file to string, then runs that string as python code.
# This lets me pull the version number on demand.
__version__ = None
exec(open('libsrd/__version__.py').read()) 

long_desc = open("README.md").read()



setup(
	name="libsrd",
	version=f"{__version__}",
	description="LibSrd is a library containing modules I use repeatedly.",
	long_description=long_desc,
	author="Sam Davis",
	author_email="sam076davis@gmail.com",
	packages=find_packages(),
	install_requires=[
		"pillow",
		"tabulate",
		"pypdf"
	],
	url="https://github.com/Samdavis112/libsrd",
	entry_points={
		'console_scripts': [
			'mergepdfs = libsrd.merge_pdf:_script',
			'imgconvert = libsrd.image_convert:_script',
			'libsrd = libsrd.__init__:_script',
		],
	},
)
