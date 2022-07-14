from setuptools import setup, find_packages

setup(
    name='montecarloPackage',
    version='1.0.0',
    url='https://github.com/kim-minah/DS5100_Final_Project.git',
    author='Minah Kim',
    author_email='mk7kc@virginia.edu',
    description='Contains montecarlo module',
    packages=find_packages(),    
    install_requires=['numpy >= 1.21.2', 'matplotlib >= 3.5.0',
                     'pandas >= 1.3.5'],
)
