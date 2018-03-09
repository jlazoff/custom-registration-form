# Imports ###########################################################

import os
from setuptools import setup


# Main ##############################################################
setup(
    name='custom-form-app',
    version='1.0',
    description='LMS - Custom Registration Extension Form',
    packages=['custom_reg_form'],
    install_requires=[
        'Django',
    ],
)