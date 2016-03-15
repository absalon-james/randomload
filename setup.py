from setuptools import setup

from randomload.meta import version

setup(
    name="randomload",
    version=version,
    author="james absalon",
    author_email="james.absalon@rackspace.com",
    packages=[
        'randomload',
        'randomload.actions',
        'randomload.actions.cinder',
        'randomload.actions.nova',
        'randomload.actions.glance'
    ],
    long_description=("Quick tool for randomly creating or deleting "
                      "servers on OpenStack."),
    data_files=[
        ('/etc/randomload', ['randomload.yaml'])
    ]
)
