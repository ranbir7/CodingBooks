from setuptools import setup

setup(
    name="lib2ran",
    version="1.0.0",
    description="Library Genesis Book Downloader by Ran7",
    author="Ranbir",
    packages=["lib2ran"],
    install_requires=[
        "libgen-api",
        "inquirer",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "lib2ran = lib2ran.__main__:main"
        ]
    },
    python_requires='>=3.7',
)
