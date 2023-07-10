from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function wil return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return(requirements)

setup(
name='mlproject',
version='0.0.1',
author='Pritesh',
author_email='priteshsingh101@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') 
# It is not feasible to write all the libraries we may require b'coz we don't know what we require
# Therefore, creating a function so it may get all the packages from requirement.txt 

)