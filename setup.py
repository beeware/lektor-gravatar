from setuptools import setup

setup(
    name='lektor-gravatar',
    version='0.1.2',
    author=u'Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='https://github.com/pybee/lektor-gravatar',
    license='MIT',
    py_modules=['lektor_gravatar'],
    entry_points={
        'lektor.plugins': [
            'gravatar = lektor_gravatar:GravatarPlugin',
        ]
    }
)
