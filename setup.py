import os
from setuptools import setup, find_packages

# Read the contents of your README file for a long description (optional).
# If you don't have a README or don't want to include a long description,
# you can omit these lines or use a simple string.
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="st-configurator",
    version="0.1.0",
    author="Frunky Liu",
    author_email="x77497856@gmail.com",
    description="A declarative and modular approach to building Streamlit apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrunkyLiu/Streamlit-Configurator",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.4.2",
    ],
    entry_points={
        "console_scripts": [
            "st-config=streamlit_configurator.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
