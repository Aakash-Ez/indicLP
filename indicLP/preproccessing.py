import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from torchtext.data.functional import sentencepiece_tokenizer
from torchtext.data.functional import load_sp_model

from gensim.models import Word2Vec
import snowballstemmer

import pickle
import os.path
import re


punctuation = """[,.;@#?!&$।|()]+\ *"""
package_directory = os.path.dirname(os.path.abspath(__file__))
supported_lang = ["hi","ta"]
langDict = {"hi":"hindi","ta":"tamil"}

class TextNormalizer:
    def __init__(self, lang = "hi"):
        assert lang in supported_lang, "Language is not supported. Currently we support the following: "+str(supported_lang)
        self.lang = lang
        self.stemmer = snowballstemmer.stemmer(langDict[lang])

    def tokenizer(self, inp_list, stem = True):
        
        inp = [re.sub(punctuation, " ", i) for i in inp_list]

        # Fetch the model from assets
        file = os.path.join(package_directory, "assets","tokenizer_models",self.lang,"token.model") 

        sp_model = load_sp_model(file)
        sp_tokens_generator = sentencepiece_tokenizer(sp_model)

        tokens = list(sp_tokens_generator(inp))
        if not stem:
            return tokens
        
        out = []
        for i in tokens:
            out.append(self.stemmer.stemWords(i))
        return out
        
    def stem(self, word):
        assert type(word) == str, "ERROR: Expected a "+str(str)+" but received a "+str(type(word))
        return self.stemmer.stemWord(word)

    def remove_stop_words(self,wordList):
        file = open(os.path.join(package_directory, "assets","stopwords",self.lang,"stopwords.pkl"),'rb')
        stopWords = pickle.load(file)
        file.close()

        out = [i for i in wordList if i not in stopWords]

        return out

class Embedding:
    def __init__(self, lang = "hi"):
        assert lang in supported_lang, "Language is not supported. Currently we support the following: "+str(supported_lang)
        self.lang = lang
        self.file_path = os.path.join(package_directory, "assets","embed_models","word2vec."+lang+".model") 
        self.model = Word2Vec.load(self.file_path)
        self.stemmer = snowballstemmer.stemmer(langDict[lang])

    def get_vector(self, word):
        assert type(word) == str, "ERROR: Expected a "+str(str)+" but received a "+str(type(word))

        word = word.replace("▁","")

        try:
            return self.model.wv[word]
        except KeyError:
            try:
                return self.model.wv[self.stemmer.stemWord(word)]
            except:
                raise KeyError("The given word is not in vocabulary.")

    def get_closest(self, word, n = 10):
        assert type(word) == str, "ERROR: Expected a "+str(str)+" but received a "+str(type(word))
        assert type(n) == int, "ERROR: Expected a "+str(int)+" but received a "+str(type(n))

        word = word.replace("▁","")

        try:
            return self.model.wv.most_similar(word, topn=n)
        except KeyError:
            try:
                return self.model.wv.most_similar(self.stemmer.stemWord(word), topn=n)
            except:
                raise KeyError("The given word is not in vocabulary.")