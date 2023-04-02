from setuptools import setup 

setup(
    name="paquete_1",
    version="1.0",
    description="Primer paquete distribuido",
    author="clase 15",
    author_email="dafbustosus@unal.edu.co",
    packages=['paquete_1']
)
# python setup.py sdist
# cd dist
# pip install paquete_1-1.0.tar.gz
