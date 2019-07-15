from setuptools import setup

with open ("README.txt", "r") as fh:
    long_description = fh.read()

setup (
    name = 'Whats_My_name',
    version = '1.0.0',
    description = 'Say my name',
    py_modules = ["script"],
    package_dir = {'new_repo': 'main'},

    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT"
    ]
    long_description = long_description,
    long_description_content_type = "text/markdown"
    
)