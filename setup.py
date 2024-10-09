from setuptools import find_packages, setup

HYPHEN_DOT_E = "-e ."

def get_requirements():

    all_requirements = []

    with open("./requirements.txt") as f:
        for line in f.readlines():
            if HYPHEN_DOT_E in line:
                continue
            all_requirements.append(line[:-1])
    
    return all_requirements

setup(
    name="MLOps",
    version="0.0.1",
    author="Jaykumar",
    author_email="jparekh4@asu.edu",
    packages=find_packages(),
    install_requires=get_requirements()
)