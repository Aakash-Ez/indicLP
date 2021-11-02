from setuptools import setup, find_packages
import os
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'indicLP',         # How you named your package folder (MyLib)
  packages = find_packages(),   # Chose the same as "name"
  version = '0.1.0a',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'indicLP is python package developed specifically to perform NLP tasks on Indic Languages like Hindi and Tamil, to make the world of AI a more inclusive space.',   # Give a short description about your library
  author = 'Aakash Ezhilan & Adityan Sunil Kumar',                   # Type in your name
  author_email = 'aakash.ezhilan@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Aakash-Ez/indicLP',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Aakash-Ez/indicLP/archive/refs/tags/main.tar.gz',    # I explain this later on
  #long_description=read('README.rst'),
  include_package_data=True,
  package_data={
    "assets":["assets/embed_models/word2vec.hi.model","assets/embed_models/word2vec.ta.model",
    "assets/stopwords/hi/stopwords.pkl",
    "assets/stopwords/ta/stopwords.pkl",
    "assets/tokenizer_models/hi/token.model",
    "assets/tokenizer_models/ta/token.model"],
  },
  keywords = ['Indic Natural Language Processing', 'Natural Language Processing', 'NLP', 'Hindi', 'Tamil', 'PyTorch'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'torch>=1.9.1',
          'torchtext>=0.10.1',
          'gensim>=4.0.0',
          'numpy>=1.19.1',
          'indic_transliteration',
          'snowballstemmer'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Intended Audience :: Science/Research',
    'Natural Language :: Tamil',
    'Natural Language :: Hindi',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)