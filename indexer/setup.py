from setuptools import setup, find_packages

setup(
    name='indexermk',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "near_lake_framework",
        "numpy",
        "matplotlib",
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
)
