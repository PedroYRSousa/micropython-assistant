from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='micropython-assistant',
    version='0.0.1',
    license='MIT License',
    author='Pedro Yago Rabelo de Sousa',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='yagosousa2512@gmail.com',
    keywords='micropython pytho micro esp32 micropy',
    description=u'Testando pypi',
    packages=['src'],
    install_requires=[],)