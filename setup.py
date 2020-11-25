from pathlib import Path

from setuptools import setup

# load long description
p = Path("README.md")
if p.exists():
    long_description = p.read_text()

setup(
    name='pythoned',
    version='0.8rc2',
    author='Edvard Rejthar',
    author_email='edvard.rejthar@nic.cz',
    url='https://github.com/CZ-NIC/pythoned',
    license='GNU GPLv3',
    description='Launch your tiny Python script on a piped in contents and pipe it out',
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=['pythoned'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
)
