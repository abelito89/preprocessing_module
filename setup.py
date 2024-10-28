from setuptools import setup, find_packages

setup(
    name="preprocessing_module",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.23.5",
        "tensorflow-gpu>=2.10.0"
    ],
    author="Abel Gomez Mendez",
    author_email="abelmetaltele@gmail.com",
    description="Preprocesses a manually loaded image to match transformations typically applied by `tf.keras.utils.image_dataset_from_directory`"
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abelito89/preprocessing_module.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)