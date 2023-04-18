# setupfile for the engine module

from distutils.core import setup

setup(name='engine',
        version='0.1',
        description='engine for jelly game',
        author='Jelly Game Team',
        install_requires=[
            'Tkinter >= 8.6.11',
            'pyaudio >= 0.2.11',
            'wave >= 0.0.2',
            'PIL >= 8.3.2'
        ],
        packages=['engine'],
        package_dir={'engine': 'engine'},
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.10.8'
        ],
        keywords='engine game',
        python_requires='>=3.9.6'

)

