from setuptools import setup, find_packages

setup(
    name='Star_BSL-Home-Assistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'BSL_Translator @ git+https://github.com/abbiereid/BSL_Translator.git@1e4ef6401964a4eccb25ab0d7875d59d5536b5a7'
    ],
)