# indicLP Library

# IndicLP Library
### _AI Development tools for Indic Languages_

Indic language processing library, is an effort to make it easy for developers and researchers to build fascinating applications and models in Indian Languages. The objective of this initiative is to develop an all encomposing library, containing the necessary tools to process language data while also methods to help in model development

## Features

|  Language  	|    Tokenization    	| Stemming 	| Embedding 	|  Datasets 	| Transliteration 	|
|:----------:	|:------------------:	|:--------:	|:---------:	|:---------:	|:---------------:	|
|  Hindi 	| ✅ 	|  ✅|✅|✅|✅|
| Tamil 	|    ✅   	|  ✅|✅|✅|✅|

Currently we support Hindi and Tamil, and are looking to support more languages in the future. We are also looking to add more features in the supported languages and improve the existing ones! 


## Tech

indicLP has been built on python as a package to help the developers easily use it's functionalities without bothering about the code. Furthermore to faciliate the intergation of deep learning models, PyTorch layers have been added in torch.nn module of indicLP and tokenization has been doing sentencepiece module of PyTorch.

Requirements:
 - Gensim >= 4.0.1
 - torchtext >= 0.10.1
 - torch >= 1.9.1
 - indic_transliteration
 - snowballstemmer
 - zipfile