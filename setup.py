import os
import re
from os import path

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


class BuildIconsCommand(build_py):
    """Custom Build Icons Command
    """
    def run(self):
        # First copy all files
        super(BuildIconsCommand, self).run()
        build_file = path.join('build', 'lib', 'flask_feather','icons.py')
        icon_dir = path.join('feather', 'icons')
        files = [f for f in os.listdir(icon_dir)
                 if path.isfile(path.join(icon_dir, f))]
        with open(build_file, 'w') as icons:
            # Open the build file once, then iterate over all icons
            for file in files:
                icon_name = str(file.split('.')[0]).replace('-', '_')
                with open(path.join(icon_dir, file), 'r') as icon:
                    svg = icon.read()
                # Modify the svg, remove line and spaces
                svg = re.sub(r'\n', r' ', svg)
                svg = re.sub(r'\s+', r' ', svg)
                svg = svg.replace('> <', '><').replace(' />', '/>')
                # Add to the build file
                icons.write("%s = \'%s\'%s" % (icon_name, svg, os.linesep))


with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'flask>=1.1',
    'Jinja2'
]

testing_extras = []

setup(
    name='flask-feather',
    version='0.1.0',
    author='Tom Vos',
    author_email='tjvos1@gmail.com',
    cmdclass={
        'build_py': BuildIconsCommand
    },
    description='A simple Tag to implement Feather Icons in Flask',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/thetomcat/flask-feather',
    # py_modules=["flask_feather"],
    package_dir= {'':'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': ["pytest>=3.7", 'twine>=3.2', 'check-manifest'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Operating System :: OS Independent",
    ]
)

