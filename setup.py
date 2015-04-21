from setuptools import setup

setup(
    name='django-rest-framework-timedeltafield',
    version='0.0.1',
    description='Django Rest Framework serializer field for timedelta fields.',
    long_description=open('README.md').read(),
    url='https://github.com/RyanPineo/django-rest-framework-timedelta-field',
    author='Ryan Pineo',
    author_email='ryanpineo@gmail.com',
    packages=[
        'timedelta_drf'
    ]
)
