import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='datec',
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
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
