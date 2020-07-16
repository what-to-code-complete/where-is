from typing import List, Dict
import setuptools  # type: ignore
import pathlib

REQUIRED: List[str] = ["rich==3.1.0", "typer==0.3.0"]
EXTRAS: Dict[str, List[str]] = {"dev": ["mypy==0.782", "pytest==5.4.3"]}

setuptools.setup(
    name="where-is",
    version=pathlib.Path("VERSION").read_text().strip(),
    description="Finds config files.",
    long_description_content_type="text/markdown",
    long_description=pathlib.Path("README.md").read_text().strip(),
    author="ALinuxPerson",
    author_email="micheal02052007@gmail.com",
    python_requires=">=3.6.0",
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    entry_points={"console_scripts": ["where-is=whereis.__main__:main"]},
    include_package_data=True,
    license="GNU GPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
