# setupfile for the jellygame module
# use command "python setup.py sdist" to create a source distribution

from distutils.core import setup

setup(name='JellyGameEngine',
        version='0.1',
        description='engine for jelly game',
        author='Jelly Game Team',
        install_requires=[
            'pyaudio >= 0.2.11',
            'wave >= 0.0.2'
        ],
        packages=['jellygame'],
        package_dir={'jellygame': '.'},
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.10.8'
        ],
        keywords='game engine',
        python_requires='>=3.9.6'

)

