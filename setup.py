from distutils.core import setup
setup(
  name = 'indicLP',         # How you named your package folder (MyLib)
  packages = ['indicLP'],   # Chose the same as "name"
  version = '0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'indicLP is python package developed specifically to perform NLP tasks on Indic Languages like Hindi and Tamil, to make the world of AI a more inclusive space.',   # Give a short description about your library
  author = 'Aakash Ezhilan & Adityan Sunil Kumar',                   # Type in your name
  author_email = 'aakash.ezhilan@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Indic Natural Language Processing', 'Natural Language Processing', 'NLP', 'Hindi', 'Tamil', 'PyTorch'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'torch>=1.9.1',
          'torchtext>=0.10.1',
          'gensim>=4.0.0',
          'numpy>=1.19.1',
          'indic_transliteration',
          'tarfile',
          'snowballstemmer',
          'zipfile'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers :: Researchers',      # Define that your audience are developers
    'Topic :: NLP :: Natural Language Processing :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)