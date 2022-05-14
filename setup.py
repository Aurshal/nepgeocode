from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="nepgeocode",
    version="1.0.0",
    long_description=long_description,
    description="A library for easy access to geological codes of district and municipalites in Nepal.",
    url="https://github.com/pypa/sampleproject",
    author="Kushal Subedi",
    author_email="kushalsubedi2@gmail.com",
    license="MIT",
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    package_data={
        "": ["*.json"],
        "": ["data/*.json", "data/*.xlsx"],
    },
    include_package_data=True,
    install_requires=[
        "openpyxl",
        "thefuzz",
    ],  # other dependencies for library to be installed
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
