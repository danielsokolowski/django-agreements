from setuptools import setup, find_packages #your system should use distribute which is successor to setuptools 
                                            # and distutils, http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-and-setuptools

package = __import__('agreements')
setup(name='django-agreements',
    install_requires=['distribute'], # let's use the enhanced setuptools
    version=package.get_version(),
    url='http://github.com/danielsokolowski/django-agreements',
    license='N/A',
    description=package.__doc__.strip(),
    author='Daniel Sokolowski ',
    author_email='stnemeerga-ognajd@danols.com',
    include_package_data=True, # this will use MANIFEST.in during install where we specify all of our additional files
    packages=find_packages(),
    # Below is not needed as we are utilizing MANIFEST.in 
    #package_data={'simplemenu': ['locale/en/LC_MESSAGES/*', 
    #                             'locale/ru/LC_MESSAGES/*']
    #              },
    scripts=[],
    requires=[],
    )