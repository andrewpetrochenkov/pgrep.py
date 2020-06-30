import setuptools

setuptools.setup(
    name='pgrep',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
