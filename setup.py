from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='sentiment_lexicon',
    version='0.2.1',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=['sentiment_lexicon'],
    url='https://github.com/emilbaekdahl/sentiment_lexicon',
    author='Emil Bækdahl',
    author_email="emilsbaekdahl@gmail.com",
    project_urls={'Source Code': 'https://github.com/emilbaekdahl/sentiment_lexicon',
                  'Documentation': 'https://emilbaekdahl.github.io/sentiment_lexicon/'}
)
