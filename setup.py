from setuptools import setup

setup(
    name='cloudify-agent-plugin',
    version='0.0.1',
    description='Writes a tmp file on agent side',
    packages=['agent_code'],
    install_requires=[
        "cloudify-plugins-common>=3.3"
    ]
)
