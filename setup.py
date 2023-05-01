# Importing Important Libraries

from setuptools import find_packages,setup
from typing import List


requirement_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

# To Get The Information From requirements.txt In String Form

def get_requirements() ->List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

    
    
    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list



# Setup and Author Details :
 
setup(name='PredictionModel',        # Ensure name must be same as project name
      version='1.0',                 # For every updation of file, Version Number must be updated 
      description='Machine Learning Prediction Model ',
      author='CHANDAN DINKAR CHAUDHARI',
      author_email='chaudhari.chandan22@gmail.com',
      url='https://github.com/chandanc5525/ML_Project',
      install_require = get_requirements(),
      packages = find_packages()     # It will find packages mentioned in requirements.txt 
     )