import os
from setuptools import setup, find_packages

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
    license="MIT",  # Explicit license declaration
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.4.2",
    ],
    entry_points={
        "console_scripts": [
            "st-config=streamlit_configurator.cli:main",
        ],
    },
    # Additional metadata fields
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="streamlit configuration declarative placeholders UI",
    python_requires=">=3.10",
)