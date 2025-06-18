from setuptools import setup, find_packages

setup(
    name='scratchuser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='VIGARPAST_777',
    author_email='vicente.garcia@colegiosocorro.org',
    description='Librería para obtener datos públicos de usuarios de Scratch',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VIGARPAST-777-2/ScratchUser-Py-Library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
