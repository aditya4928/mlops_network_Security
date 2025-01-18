from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return lsit of requirements.
    """
    requirement_list:List[str]=[]
    try:
        with open('requirement.txt','r') as file:
            #Read lines from files
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file is not found")
    return requirement_list

setup(

    name="network_security",
    version="0.1",
    author="Aditya Pratap Singh",
    author_email="pratapaditya521@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



