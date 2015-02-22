from setuptools import setup


long_description = ""

setup(
    name="aiomultiprocessing",
    version="0.1",
    scripts=[],
    packages=['aiomultiprocessing'],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='n/a',
    license="Expat",
    url="http://pault.ag/",
    platforms=['any'],
    entry_points={
        'console_scripts': [
            'dionysus = dionysus.cli:main',
        ],
    }
)
