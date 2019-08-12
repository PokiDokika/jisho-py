import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jishopy",
    version="0.0.1.1",
    author="Poki",
    author_email="poki@tuta.io",
    description="A simple Python wrapper for the API of Jisho.org",
    url="https://github.com/PokiDokika/jisho-py",
    license='MIT',
    keywords='jisho api python wrapper',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
