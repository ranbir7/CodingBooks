from setuptools import setup

setup(
    name="lib2ran",
    version="0.1",
    packages=["lib2ran"],  # updated from "lib" to "lib2ran"
    install_requires=[
        "libgen-api",
        "inquirer",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "lib2ran = lib2ran.__main__:main"  # updated from "lib" to "lib2ran"
        ]
    },
)
