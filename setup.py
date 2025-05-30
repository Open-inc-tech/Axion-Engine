from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    long_desc = f.read()

setup(
    name='Axion-Engine',
    description='A gui game maker written in python',
    long_description=long_desc,
    long_description_content_type="text/markdown",

    version='0.0.2',
    author='The_Sun_Kitsune',
    license='MIT',
    keywords='game development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'panda3d',
        'panda3d-gltf',
        'pillow',
        'pyperclip',
        'screeninfo',
        'psutil',
        'ursina'
    ],

    python_requires='>=3.10',
)
