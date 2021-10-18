from setuptools import find_packages, setup

setup(
    name='widgets_and_gadets_backend',
    version='0.1',
    description='',
    url='widgetsandgadgetsltd.com',
    author='Zach Smith',
    author_email='zlynn100@gmail.com',
    license='n/a',
    packages=find_packages(),
    package_data={
        'src': ['*.json']
    },
    include_package_data=True
)