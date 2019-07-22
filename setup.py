import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='datec-isaacto',
    version='0.1',
    author='Isaac To',
    author_email='isaac.to@gmail.com',
    description='Date Command',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/isaacto/datec',
    packages=setuptools.find_packages(),
    install_requires=[
        'python-dateutil'
    ],
    entry_points={
        "console_scripts": [
            "datec=datec.__main__:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
