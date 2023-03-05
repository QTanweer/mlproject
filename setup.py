from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .' # Hyphen e dot in the requirements.txt file does nothing but returns back to this setup file to build this project like a package


def get_requirements(file_path:str) -> List[str]:
    '''
    this function takes a file path and returns a list of requirements
    '''  
    requirements = []   
    with open(file_path, 'r') as file_object:
        requirements = file_object.read().splitlines()
    
    if HYPHEN_E_DOT in requirements:      # ignore hyphen e . in requirements list as hyphen e . is written at the end of requirements.txt file
        requirements.remove(HYPHEN_E_DOT)
    return requirements

    


setup(
    name='mlproject',
    version='0.1',
    author= 'Qamar Malik',
    author_email= 'qtanweer.mts41ceme@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt') # this will install all the requirements from requirements.txt file
)