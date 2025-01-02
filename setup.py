from setuptools import setup


setup(
    name='PWE',
    version='1.0.0',
    description='A Python game framework using SDL',
    long_description="A Python game framework using SDL library for creating 2D games",
    author='Paulo Matheus',
    author_email='jclodoaldosantana204@gmail.com',
    url='https://github.com/Peixe2b/PWE',
    packages=['PWE'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Programming Language :: Python :: 3.12.1',
        'License :: Apache License',
        'Operating System :: Linux',
    ],
    python_requires='>=3.12',
    install_requires=['ctypes'],
    entry_points={
        'console_scripts': [
            'pwe_run=PWE.pwe_run:main'
        ]
    },
    zip_safe=False,
)
