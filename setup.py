from setuptools import find_packages, setup

# with open("README.md", encoding="utf-8") as f:
#     long_description = f.read()

setup(
    name="st-configurator",
    version="0.1.0",
    author="Frunky Liu",
    author_email="x77497856@gmail.com",
    description="快速且可重複利用的 Streamlit UI 建構工具",
    # long_description=long_description,
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
