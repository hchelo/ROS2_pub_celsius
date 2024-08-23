from setuptools import find_packages, setup

package_name = 'fahrenheit'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kubu',
    maintainer_email='hiperchelo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker2 = fahrenheit.pub_temp_celsius:main',
        	'listener2 = fahrenheit.sus_pub_temp_fahrenheit:main',
        	'talker3 = fahrenheit.sus_pub_temp_fahrenheit:main',
        	'listener3 = fahrenheit.sus_nuevo:main',
        ],
    },
)
