from setuptools import setup

setup(
    name = 'meshblu',
    packages = ['meshblu'], # this must be the same as the name above
    version = '0.1',
    description = 'Meshblu HTTP RESTful Python client',
    author = 'Drasko DRASKOVIC',
    author_email = 'drasko.draskovic@gmail.com',
    url = 'https://github.com/drasko/meshblu-py', # use the URL to the github repo
    keywords = ['iot', 'meshblu', 'http'], # arbitrary keywords
    long_description = """Meshblu (https://github.com/octoblu/meshblu) HTTP RESTful Python client""",
    classifiers = [
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
    ],
    install_requires = [
        "requests",
    ],
    license = 'MIT',
    test_suite = 'tests'
)
