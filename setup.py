# we use it becoz of buliding our application as packege it self

# The setup.py file is used to package and distribute Python projects — especially when you're creating a reusable module or library.

# When to use setup.py:
# You want to convert your code into a package others (or even you) can install with pip.

# You're working on a modular project or library (like a Python module, ML pipeline, or CLI tool).

# You're building a project that you plan to:

# Publish on PyPI

# Share with your team

# Use across multiple projects

from setuptools import setup, find_packages

# Function to read requirements.txt
HYPEN_E_DOT = '-e .'

def get_requirements(file_path='requirements.txt'):
    requirements = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#') and line != HYPEN_E_DOT:
                requirements.append(line)
    return requirements


# Setup configuration
setup(
    name='ml_project',
    version='0.1',
    author='Soham_Adchule',
    author_email='sohamadchule@gmail.com',
    description='An end to end ML project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)