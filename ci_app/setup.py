from setuptools import setup

setup(
    name='cd_web_server',
    version='0.0.1',
    author='dementevda',
    packages=['ci_app'],
    install_requires=['Flask', 'docker', 'urllib3=1.26.14'],
    include_package_data=True,
    keywords=[
        'ci', 'github actions', 'flask', 'docker'
    ],
    entry_points={
        'console_scripts': [
            'cd_web_server = ci_app.app:main']},
)

