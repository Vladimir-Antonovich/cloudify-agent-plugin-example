from setuptools import setup

setup(
    name='cloudify-agent-plugin-example',
    version='0.0.2',
    description='Writes a tmp file on agent side',
    packages=['agent_code'],
    install_requires=[
        "cloudify-common>=5.1"
    ]
)
