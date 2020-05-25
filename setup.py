#!/usr/bin/env python
from setuptools import setup, find_packages


def main():
    skw = dict(
        name="ci-skeleton-demo",
        version='0.0.0',
        description="A dummy package for conda-smithy CI skeleton",
        author="CJ Wright",
        packages=["ci_skeleton_demo"],
    )
    setup(**skw)


if __name__ == "__main__":
    main()
