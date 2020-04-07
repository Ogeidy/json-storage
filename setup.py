from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="json-storage",
    version="0.1",
    author="Yakov Mamontov",
    author_email="yakov-mamontov@yandex.ru",
    description="Web service for storing JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ogeidy/json-storage",
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Flask>=1.1.2',
        'Flask-SQLAlchemy>=2.4.1',
        'psycopg2-binary>=2.8.5'
    ],
    python_requires='>=3.6',
)
