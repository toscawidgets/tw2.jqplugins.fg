from setuptools import setup, find_packages

import multiprocessing, logging

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

# Requirements to install buffet plugins and engines
_extra_genshi = ["Genshi >= 0.3.5"]
_extra_mako = ["Mako >= 0.1.1"]

setup(
    name='tw2.jqplugins.fg',
    version='2.0b9',
    description='toscawidgets2 wrapper for random filament group tools',
    long_description=long_description,
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    license='MIT',
    url='http://github.com/ralphbean/tw2.jqplugins.fg',
    install_requires=[
        "tw2.core>=2.0b5",
        "tw2.jquery",
        "tw2.jqplugins.ui>=2.0b21",
        ],
    extras_require = {
        'genshi': _extra_genshi,
        'mako': _extra_mako,
    },
    tests_require = ['BeautifulSoup', 'nose', 'FormEncode', 'strainer', 'WebTest',] + _extra_genshi + _extra_mako,
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jqplugins.fg
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
