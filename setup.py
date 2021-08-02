
"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace('\n', '') for lib in requirements_list]

requirements = requirements_list

test_requirements = []

setup(
    author="Bethelhem Sisay",
    author_email="sisaybethelhem@gmail.com",
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Pharmaceutical Sales prediction",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts',
    name='scripts',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='Tests',
    tests_require=test_requirements,
    url='https://github.com/Bethelsis/Pharmaceutical-Sales-prediction/',
    version='0.1.0',
    zip_safe=False,
)
