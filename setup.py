import os
import setuptools


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setuptools.setup(
    name='django-newapp',
    version='0.9.1',
    packages=setuptools.find_packages(),  # ['push'],
    include_package_data=True,
    license='BSD',
    description='Django reusable app, what allows to create app with non standard template',
    long_description=README,
    long_description_content_type="text/x-rst",
    author='Bramandityo Prabowo',
    author_email='freez.meinster@gmail.com',
    url='https://github.com/freezmeinster/django-newapp',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=2.2'
    ]
)
