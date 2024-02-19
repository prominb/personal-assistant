from setuptools import setup, find_namespace_packages

setup(
    name='useful',
    version='0.0.1',
    description='Very useful code',
    url='https://github.com/basilegupov/personal-notebook',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['run-assistant = src.main:main']},  # run-helper
    zip_safe=False  # True
)