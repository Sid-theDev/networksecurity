'''
This file is an essential part of packaging tools 
and distributing python projects. 
it is used by setuptools to define configuration of
your project such as its metadata, dependencies and more.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Processing each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
            
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="a",
    author_email="xyz@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)