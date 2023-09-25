from setuptools import setup, find_packages

setup(
    name='my_python_project',
    version='0.1.0',
    description='My Python Project Description',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        # Add 'matplotlib' to the list of dependencies
        'matplotlib',
        # Add other dependencies as needed
    ],
)
