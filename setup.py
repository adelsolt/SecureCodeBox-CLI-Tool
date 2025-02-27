from setuptools import setup, find_packages

setup(
    name="securecodebox-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pyyaml"],
    entry_points={
        "console_scripts": [
            "scbcli=scbcli.main:main",
        ],
    },
    author="Adel Soltane",
    author_email="soltane.adel@hotmail.com",
    description="A SecureCodeBox CLI tool for managing scans in Kubernetes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/adelsolt/securecodebox-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    data_files=[("share/man/man1", ["docs/scbcli.1"])],  # Optional man page
)
