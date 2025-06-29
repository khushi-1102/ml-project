from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """This function returns the list of requirements."""
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n,'"") for req in requirements]
    return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="khushi",
    author_email="khushisokaria@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirment.txt")
)