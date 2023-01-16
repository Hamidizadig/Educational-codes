from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()
print(required)
setup(
    name='xPackage' ,
    version='0.1.0' ,
    author='HamidIzadi' ,
    author_email='izadhaaa@gmail.com' ,
    description='Hello' ,
    long_description=open(README.txt).read() ,
    python_requires='>=3.8',
    packages=['mypackage'] ,
    install_requires=required ,
    
)    
    